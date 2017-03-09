## Usage: Rscript ../benchmark.R -i closed_reference_otus_1234.txt -f WATER_CONTENT_SOIL
library(optparse)
source('~/softwares/my/ml_util.R')

opt <- interface_generalize()

if (opt$debug) save.image('debug.Rdata')

if (opt$verbose) {
    cat("Running command with args:\n",
        paste(commandArgs(), collapse = " "),
        '\n')
}


if (opt$split <= 0 & opt$split > 1) {
    stop("The split arg should be greater than 0 and not greater than 1.")
}

if(is.null(opt$models)) {
    models <- regression
} else {
    models <- strsplit(opt$models, ',')[[1]]
}


library(caret)
if (opt$cores > 1) {
    library(doMC)
    registerDoMC(opt$cores)
}

meta <- read.table.x(opt$metadata)
meta.col <- colnames(meta)
if (is.null(opt$fields)) {
    stop("No field is provided to do regression on.")
}
outcome.col <- strsplit(opt$fields, ',')[[1]]
x <- which(! outcome.col %in% meta.col)
if (length(x) > 0) {
    stop("Field(s) ", paste(outcome.col[x], collapse=','), " do not exist in meta data")
}

meta.2 <- read.table.x(opt$metadata_2)
meta.col.2 <- colnames(meta.2)
if (is.null(opt$fields)) {
    stop("No field is provided to do regression on.")
}
x <- which(! outcome.col %in% meta.col.2)
if (length(x) > 0) {
    stop("Field(s) ", paste(outcome.col[x], collapse=','), " do not exist in meta data 2")
}

## extract part of the samples by their meta data
if (! is.null(opt$category)) {
    ## e.g. "SITE::nostril,skin;SEX::male"
    extract <- strsplit(opt$category, ':_:')[[1]]
    extract <- strsplit(extract, '::')
    for (x in extract) {
        if (! x[1] %in% meta.col)
            stop("The field ", x[1], " does not exist in meta data")
        i <- meta[[ x[1] ]]
        j <- strsplit(x[2], ',')[[1]]
        if (! all(j %in% i)) {
            ## insanity check to avoid typos
            stop("You specified non-existing values for field ", x[1], " in meta data")
        }
        meta <- meta[ i %in% j, ]

        if (! x[1] %in% meta.col.2)
            stop("The field ", x[1], " does not exist in meta data 2")
        i <- meta.2[[ x[1] ]]
        j <- strsplit(x[2], ',')[[1]]
        if (! all(j %in% i)) {
            ## insanity check to avoid typos
            stop("You specified non-existing values for field ", x[1], " in meta data 2")
        }
        meta.2 <- meta.2[ i %in% j, ]
    }
}


if (! is.null(opt$numeric)) {
    ## e.g. "PH::6,12;TEMP::,32"
    extract <- strsplit(opt$numeric, ':_:')[[1]]
    extract <- strsplit(extract, '::')
    for (x in extract) {
        if (! x[1] %in% meta.col)
            stop("The field ", x[1], " does not exist in meta data")
        ## in case there is None, NA, etc in the column (R will read it into character
        ## instead of numerical)
        i <- as.numeric(as.character(meta[[ x[1] ]]))
        j <- as.numeric(strsplit(x[2], ',')[[1]])
        ## NA & TRUE -> NA
        ## NA & FALSE -> FALSE
        n <- rep(T, nrow(meta))
        if (! is.na(j[1]))
            n <- n & i >= j[1]
        if (! is.na(j[2]))
            n <- n & i <= j[2]
        meta <- meta[n, ]
    }
}

if (! is.null(opt$numeric2)) {
    ## e.g. "PH::6,12;TEMP::,32"
    extract <- strsplit(opt$numeric2, ':_:')[[1]]
    extract <- strsplit(extract, '::')
    for (x in extract) {
        if (! x[1] %in% meta.col.2)
            stop("The field ", x[1], " does not exist in meta.2 data")
        ## in case there is None, NA, etc in the column (R will read it into character
        ## instead of numerical)
        i <- as.numeric(as.character(meta.2[[ x[1] ]]))
        j <- as.numeric(strsplit(x[2], ',')[[1]])
        ## NA & TRUE -> NA
        ## NA & FALSE -> FALSE
        n <- rep(T, nrow(meta.2))
        if (! is.na(j[1]))
            n <- n & i >= j[1]
        if (! is.na(j[2]))
            n <- n & i <= j[2]
        meta.2 <- meta.2[n, ]
    }
}


otus <- read.table.x(opt$input_otu_table)


tax.16s <- otus[, length(otus)]
tax.16s <- gsub("^Root; ", "", tax.16s)
## insert a newline for every three levels of taxonomy
tax.16s <- gsub("([^;]*); ([^;]*); ([^;]*); ", '\\1; \\2; \\3\n', tax.16s)
names(tax.16s) <- otus[[1]]


## remove the 6-digit suffix of the sample IDs in the mapping file.
## meta.sid <- gsub(".[0-9]{6}$", "", as.character(meta[[1]]))
meta.sid <- as.character(meta[[1]])
rownames(meta) <- meta.sid
sample.ids <- intersect(meta.sid, colnames(otus))
meta <- meta[sample.ids, ]


rownames(otus) <- otus[[1]]
otus <- data.frame(t(otus[, sample.ids]), check.names=FALSE)


otus.2 <- read.table.x(opt$input_otu_table_2)
meta.sid <- as.character(meta.2[[1]])
rownames(meta.2) <- meta.sid
sample.ids <- intersect(meta.sid, colnames(otus.2))
meta.2 <- meta.2[sample.ids, ]

rownames(otus.2) <- otus.2[[1]]
otus.2 <- data.frame(t(otus.2[, sample.ids]), check.names=FALSE)


## add numeric fields as predictors
if (! is.null(opt$add_numeric)) {
    add.pred <- strsplit(opt$add_numeric, ',', fixed=TRUE)[[1]]
    not.in <- which(! add.pred %in% colnames(meta))
    if (length(not.in) > 0) {
        stop(paste(c(add.pred[not.in], "not in the meta data!!!"), collapse=' '))
    }
    otus <- cbind(as.numeric(meta[, add.pred]), otus)
    colnames(otus)[1:length(add.pred)] <- add.pred

    not.in <- which(! add.pred %in% colnames(meta.2))
    if (length(not.in) > 0) {
        stop(paste(c(add.pred[not.in], "not in the meta data 2!!!"), collapse=' '))
    }
    otus.2 <- cbind(as.numeric(meta.2[, add.pred]), otus.2)
    colnames(otus.2)[1:length(add.pred)] <- add.pred
}
## add the categorical fields in the meta data as predictors
if (! is.null(opt$add_category)) {
    add.pred <- strsplit(opt$add_category, ',', fixed=TRUE)[[1]]
    not.in <- which(! add.pred %in% colnames(meta))
    if (length(not.in) > 0) {
        stop(paste(c(add.pred[not.in], "not in the meta data!!!"), collapse=' '))
    }
    if (opt$debug) save.image('debug.Rdata')
    x <- meta[, add.pred, drop=FALSE]
    dummy <- dummyVars(~., data=x)
    otus <- cbind(predict(dummy, x), otus)

    not.in <- which(! add.pred %in% colnames(meta.2))
    if (length(not.in) > 0) {
        stop(paste(c(add.pred[not.in], "not in the meta data 2!!!"), collapse=' '))
    }
    if (opt$debug) save.image('debug.Rdata')
    x <- meta.2[, add.pred, drop=FALSE]
    dummy <- dummyVars(~., data=x)
    otus.2 <- cbind(predict(dummy, x), otus.2)
}

otu.ids <- intersect(colnames(otus), colnames(otus.2))
otus <- otus[, otu.ids]
otus.2 <- otus.2[, otu.ids]

pdf(sprintf("%s.pdf", opt$output))

for(label in outcome.col) {
    if(opt$verbose)
        cat("=========", label, ":\n")

    outcome <- as.numeric(as.character(meta[[label]]))

    if(opt$verbose) {
        cat("---- a glimpse of outcome:\n")
        print(head(outcome, n=30))
    }

    ## remove NA values
    outcome.na <- is.na(outcome)
    ## if more than half of the samples are not numeric
    if(sum(outcome.na) > 0.5 * length(outcome)) {
        if(opt$verbose)
            cat("outcome has less than half of numeric values. skip it.\n")
        next
    }

    outcome <- outcome[! outcome.na]
    ## if there less than 5 uniq values in this category
    if(length(unique(outcome)) < 3) {
        if(opt$verbose)
            cat("outcome has less than 3 distinctive values. skip it.\n")
        next
    }

    train.set <- otus[! outcome.na, ]


    if (opt$split < 1) {
        set.seed(1)
        training.rows <- createDataPartition(outcome, p=opt$split, list=F)
    } else {
        training.rows <- 1:length(outcome)
    }

    train.full <- train.set[training.rows, ]
    test.full <- train.set[-training.rows, ]
    train.outcome <- outcome[training.rows]
    test.outcome <- outcome[-training.rows]

    nzv <- nearZeroVar(train.full)
    if (length(nzv) > 0) {
        train.full <- train.full[, -nzv]
        test.full <- test.full[, -nzv]
    }
    tooHigh <- findCorrelation(cor(train.full), .9)
    if (length(tooHigh) > 0) {
        train.full <- train.full[, -tooHigh]
        test.full <- test.full[, -tooHigh]
    }

    ## save the test set results in a data.frame
    if (length(test.outcome) > 0)
        testResults <- data.frame(obs=test.outcome)

    gen.testX <- otus.2[, colnames(train.full), drop=FALSE]
    gen.testY <- as.numeric(as.character(meta.2[[label]]))
    gen.results <- data.frame(obs=gen.testY)

    if (opt$debug) save.image('debug.Rdata')

    ## benchmark the specified models
    tuned.list <- list()
    accuracies <- data.frame()

    for (model in models) {
        tuned <- regression.tune(train.full, train.outcome, model)
        ## if(is.na(tuned) | is.null(tuned)) next
        if (class(tuned) != 'train') {
            cat("Warning message:\nModel ", model, " failed.\n")
            next
        }
        tuned.list[[model]] <- tuned
        accu <- accuracy(tuned)

        if (opt$verbose) {
            print(tuned)
            print(accu)
        }
        ## add a new column - Model
        tuned$resample$Model <- model
        accuracies <- rbind(accuracies, tuned$resample)

        if (length(test.outcome) > 0)
            testResults[model] <- predict(tuned, test.full)
        imp <- varImp(tuned)
        pimp <- plot.imp(imp, tax.16s, main=model)
        print(pimp, position=c(0, 0, 0.56, 1))

        gen.results[model] <- predict(tuned, gen.testX)

        if (opt$debug) save.image(sprintf("%s.Rdata", opt$output))
    }

    if (opt$debug) save.image('debug.Rdata')

    if (ncol(gen.results) > 1)
        y.yhat(gen.results)

    if (opt$diagnostic) {
        diagn <- diagnostics(train.full, train.outcome, gen.testX, gen.testY)
    }

    if (length(tuned.list) > 1) {
        ## compare the model performances
        resamp <- resamples(tuned.list)
        m.diff <- diff(resamp)
        if (opt$verbose) print(summary(m.diff))
        print(dotplot(m.diff))
    }

    ## plot yhat vs. obs
    if (length(test.outcome) > 0) {
        y.yhat(testResults)
    }
}

dev.off()

save.image(sprintf("%s.Rdata", opt$output))

