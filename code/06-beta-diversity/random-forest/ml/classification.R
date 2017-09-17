## get the path of this very script
args <- commandArgs(trailingOnly = F)
scriptPath <- normalizePath(dirname(sub("^--file=", "", args[grep("^--file=", args)])))
source(paste(scriptPath, 'ml_util.R', sep='/'))


for(label in outcome.col) {
    if(opt$verbose)
        cat("=========", label, ":\n")

    outcome <- as.character(meta[[label]])
    ## the space in the class names cause problem for some models
    outcome <- as.factor(gsub("[[:space:]]+", "_", outcome))

    ## remove NA values
    outcome.na <- is.na(outcome)
    not.na <- (! outcome.na) & complete.cases(otus)

    ## if more than half of the samples are not numeric
    ## if(sum(not.na) < 0.5 * length(outcome)) {
    ##     if(opt$verbose)
    ##         cat("outcome has less than half of numeric values. skip it.\n")
    ##     next
    ## }
    if (! is.null(opt$replicate)) {
        replicate <- replicate[not.na]
        uniq_rep <- unique(replicate)
        ## create 5-repeat 10 folds
        idx_rep <- createMultiFolds(uniq_rep)
        idx <- lapply(idx_rep,
                      function (i) {
                          reps <- uniq_rep[i]
                          which(replicate %in% reps)
                      })
    } else {
        idx <- NULL
    }
    outcome <- outcome[not.na]
    if (opt$verbose) {
        cat("---- a glimpse of outcome:\n")
        print(table(outcome))
    }
    if (opt$debug) save.image('debug.Rdata')
    if (length(outcome) < min.sample.size)
        stop("There should be more than ", min.sample.size, " samples.")

    ## if there less than 2 classes in this category
    if (nlevels(outcome) < 2) {
        if(opt$verbose)
            cat("outcome has less than 2 classes. skip it.\n")
        next
    }

    train.set <- otus[not.na, ]


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

    if (opt$debug) save.image('debug.Rdata')

    nzv <- nearZeroVar(train.full, freqCut = 99/1, uniqueCut = 1)
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

    if (opt$debug) save.image('debug.Rdata')

    ## benchmark the specified models
    tuned.list <- list()
    accu <- data.frame()
    top.f <- data.frame()
    for (model in models) {
        if (opt$feature_selection) {
            fiveStats <- function(...) c(twoClassSummary(...), defaultSummary(...))
            ctrl <- rfeControl(method = "repeatedcv",
                               repeats = 5, number=10,
                               index = idx,
                               saveDetails = TRUE)
            ## random forest
            ctrl$functions <- rfFuncs
            if (nlevels(train.outcome) == 2) {
                ctrl$functions$summary <- fiveStats
            } else {
                ctrl$functions$summary <- defaultSummary
            }
            set.seed(721)
            tuned <- rfe(train.full,
                         train.outcome,
                         sizes = seq(10, ncol(train.full)-10, by=10),
                         metric = "Kappa",
                         ntree = 1000,
                         rfeControl = ctrl)
            tuned$method = 'rf'
        } else {
            save.image('debug.Rdata')
            tuned <- classification.tune(train.full, train.outcome, model, ctrl=opt$cv, idx=idx)
            save.image('debug.Rdata')
            cm.plot <- cm.result(caret::confusionMatrix(tuned), title=paste(label, model))
            print(cm.plot)
            ## if(is.na(tuned) | is.null(tuned)) next
            if (class(tuned) != 'train') {
                cat("Warning message:\nModel ", model, " failed.\n")
                next
            }
        }

        tuned.list[[model]] <- tuned

        if (opt$verbose) {
            print(tuned)

        }

        save.image(sprintf("%s.Rdata", output))

        ## add a new column - Model
        accu <- rbind(accu, cbind(tuned$resample, Model=tuned$method))

        if (length(test.outcome) > 0)
            testResults[model] <- predict(tuned, test.full)
        imp <- varImp(tuned)
        top.f <- rbind(top.f,
                       data.frame(imp$importance[order(imp$importance,
                                                       decreasing=T),,drop=FALSE],
                                  Model=model))
        ## plot top features
        pimp <- plot.imp(imp, tax.16s, main=model)
        print(pimp, position=c(0, 0, 0.56, 1))

        save.image(sprintf("%s.Rdata", output))
    }
    accu$Field <- label
    accuracies <- rbind(accuracies, accu)
    top.f$Field <- label
    top.features <- rbind(top.features, top.f)

    ## if (opt$verbose) print(accuracies)

    big.tuned.list[[label]] <- tuned.list

    if (length(tuned.list) > 1) {
        ## compare the model performances
        resamp <- resamples(tuned.list)
        m.diff <- diff(resamp)
        if (opt$verbose) print(summary(m.diff))
        print(dotplot(m.diff))
    }

    ## plot yhat vs. obs
    if (length(test.outcome) > 0) {
        method.names <- names(testResults)
        obs <- testResults[,1]
        for(i in 2:length(testResults)) {
            pred <- testResults[,i]
            plot(pred ~ obs,
                 xlab=method.names[1], ylab=method.names[i])
            abline(0, 1, col="red")
            ## mtext(paste(c("RMSE=", "R^2="),
            ##             c(RMSE())))
            rmse <- format(round(caret::RMSE(pred, obs), 2), nsmall=2)
            rsq <- format(round(caret::R2(pred, obs), 2), nsmall=2)
            legend("topleft", text.col="blue", "ab",
                   paste(c("RMSE","R^2 "), c(rmse, rsq), sep='=', collapse='\n'))
        }
    }
}

dev.off()

save.image(sprintf("%s.Rdata", output))
