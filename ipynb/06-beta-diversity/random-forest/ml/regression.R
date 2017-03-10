## get the path of this very script
args <- commandArgs(trailingOnly = F)
scriptPath <- normalizePath(dirname(sub("^--file=", "", args[grep("^--file=", args)])))
source(paste(scriptPath, 'ml_util.R', sep='/'))


for(label in outcome.col) {
    if(opt$verbose)
        cat("=========", label, ":\n")

    outcome <- as.numeric(as.character(meta[[label]]))

    if(opt$verbose) {
        cat("---- a glimpse of outcome:\n")
        print(head(outcome, n=30))
        print(summary(outcome))
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
    if (length(outcome) < min.sample.size)
        stop("There should be more than ", min.sample.size, " samples.")

    ## if there less than 3 uniq values in this category
    if(length(unique(outcome)) < 2) {
        if(opt$verbose)
            cat("outcome has less than 2 distinctive values. skip it.\n")
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

    if (opt$debug) save.image('debug.Rdata')

    ## benchmark the specified models
    tuned.list <- list()
    accu <- data.frame()
    top.f <- data.frame()
    for (model in models) {
        if (opt$feature_selection) {
            ctrl <- rfeControl(method = "repeatedcv",
                               repeats = 5, number=10,
                               saveDetails = TRUE)
            ctrl$functions <- rfFuncs
            set.seed(721)
            tuned <- rfe(train.full,
                         train.outcome,
                         sizes = seq(10, ncol(train.full)-10, by=10),
                         metric = "RMSE",
                         ntree = 1000,
                         rfeControl = ctrl)


        } else {
            tuned <- regression.tune(train.full, train.outcome, model)
            ## if(is.na(tuned) | is.null(tuned)) next
            if (class(tuned) != 'train') {
                cat("Warning message:\nModel ", model, " failed.\n")
                next
            }
        }

        tuned.list[[model]] <- tuned

        if (opt$verbose) {
            print(tuned)
            print(accuracy(tuned))
        }

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
        pimp <- plot.imp(imp, tax.16s, main=paste(label, model))
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
        m.diff <- diff(resamp, metric='RMSE')
        if (opt$verbose) print(summary(m.diff))
        print(dotplot(m.diff, main=label))
    }

    ## plot yhat vs. obs
    if (length(test.outcome) > 0) {
        method.names <- names(testResults)
        obs <- testResults[,1]
        for(i in 2:length(testResults)) {
            pred <- testResults[,i]
            plot(pred ~ obs, main = label,
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
