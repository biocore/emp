interface_generalize <- function() {
    library(optparse)
    meta.fp <- 'mapping_file.txt'
    otus.fp <- 'closed_reference_otu_table_rare.txt'
    n.cores <- 12

    ## common models
    regression <- c("pls", "mars", "svm_rb", "svm_poly", "svm_linear", "knn", "cart", "rf", "cubist", "gbm")

    option_list <- list(make_option(c("-i", "--input_otu_table"), default=otus.fp,
                                    action="store", type="character",
                                    help="Input OTU table [default %default]"),
                        make_option(c("-m", "--metadata"), default=meta.fp,
                                    action="store", type="character",
                                    help="Mapping file [default %default]"),
                        make_option(c("--input_otu_table_2"), default=otus.fp,
                                    action="store", type="character",
                                    help="Input OTU table [default %default]"),
                        make_option(c("--metadata_2"), default=meta.fp,
                                    action="store", type="character",
                                    help="Mapping file [default %default]"),

                        make_option(c("-f", "--fields"),  default=NULL,
                                    action="store", type="character",
                                    help="Fields or categories to test [default %default]"),
                        make_option(c("-r", "--models"),  default=NULL,
                                    action="store", type="character",
                                    help=paste("Regression models to use.",
                                        "It can be pls, mars, nnet, svm_rb, svm_poly, svm_linear,",
                                        "knn, cart, m5, ctree, rf, cubist, and gbm. [default %default]",
                                        "If no modes are specified, it run all the common models: ",
                                        paste(regression, collapse=', '),
                                        sep='\n\t\t')),
                        make_option(c("-o", "--output"), default=NULL,
                                    action="store", type="character",
                                    help="Output file names. [default %default]. It will save pdf and Rdata files."),
                        make_option(c("--cv"), default=NULL,
                                    action="store", type="character",
                                    help="CV scheme. [default %default]."),
                        make_option(c("-c", "--cores"), default=n.cores,
                                    action="store", type="integer",
                                    help="Number of CPU cores [default %default]"),
                        make_option(c("-s", "--split"), default=1,
                                    action="store", type="double",
                                    help=paste("Split a only fraction of data as training set and",
                                        "hold out the rest for final testing. It should be between 0",
                                        "and 1. [default %default].",
                                        sep='\n\t\t')),
                        make_option(c("--category"), default=NULL,
                                    action="store", type="character",
                                    help=paste("Provide a category and a value to extract the samples",
                                        "of that category which has the value. For example,",
                                        "'SITE::nostril,skin' will only use the samples that are collected",
                                        "from nostril and skin.",
                                        sep='\n\t\t')),
                        make_option(c("--numeric"), default=NULL,
                                    action="store", type="character",
                                    help=paste("Similar to the '--category' but applies to numeric meta data",
                                        "For example, 'PH::6,12' will only use the samples with PH between 6 and 12 (not including 6 and 12);",
                                        "'DAYS::,16' will only use the samples with days less than 16. [default %default]",
                                        sep='\n\t\t')),
                        make_option(c("--numeric2"), default=NULL,
                                    action="store", type="character",
                                    help=paste("Similar to the '--category' but applies to numeric meta data",
                                        "For example, 'PH::6,12' will only use the samples with PH between 6 and 12 (not including 6 and 12);",
                                        "'DAYS::,16' will only use the samples with days less than 16. [default %default]",
                                        sep='\n\t\t')),
                        make_option(c("--add_category"), default=NULL,
                                    action="store", type="character",
                                    help="Add the categorical field in metadata as preditors"),
                        make_option(c("--add_numeric"), default=NULL,
                                    action="store", type="character",
                                    help="Add the numeric field in metadata as preditors"),
                        make_option(c("--file"), default=NULL,
                                    action="store", type="character",
                                    help="Add the numeric field in metadata as preditors"),
                        make_option(c("-v", "--verbose"), default=TRUE,
                                    action="store_true", type="logical",
                                    help="Output running infomation? [default %default]"),
                        make_option(c("--diagnostic"), default=FALSE,
                                    action="store_true", type="logical",
                                    help="Output running infomation? [default %default]"),
                        make_option(c("-d", "--debug"), default=FALSE,
                                    action="store_true", type="logical",
                                    help="Output running infomation? [default %default]"))

    args <- commandArgs(trailingOnly=T)
    x <- which(args %in% "--file")

    if (length(x) > 0) {
        file.arg <- args[x+1]
        if (file.exists(file.arg)) {
            args <- c(args, scan(file.arg, what='character'))
        } else {
            stop("The args file ", file.arg, " does not exist.")
        }
    }

    opt <- parse_args(OptionParser(usage = "Rscript %prog [options] file.",
                                   description = paste("Example:",
                                       "# Run on date and sex with cubist and random forest models",
                                       "Rscript %prog -f DATE,SEX -r cubist,rf",
                                       "# Run on PH with random forest model and save output rf.Rdata and rf.pdf",
                                       "Rscript %prog -f PH -r rf -o rf",
                                       sep="\n\t"),
                                   option_list = option_list),
                      args=args)
    opt
}

interface <- function() {
    library(optparse)
    meta.fp <- 'mapping_file.txt'
    otus.fp <- 'closed_reference_otu_table_rare.txt'
    n.cores <- 12

    ## common models
    regression <- c("pls", "mars", "svm_rb", "svm_poly", "svm_linear", "knn", "cart", "rf", "cubist", "gbm")
    classification <- c("pls", "glm", "lda", "glmnet", "pam", "fda", "svmRadial", "knn", "nb", "mda", "sparseLDA", "PART", "C5.0Rules", "rf", "gbm")
    option_list <- list(make_option(c("-i", "--input_otu_table"), default=otus.fp,
                                    action="store", type="character",
                                    help="Input OTU table [default %default]"),
                        make_option(c("-m", "--metadata"), default=meta.fp,
                                    action="store", type="character",
                                    help="Mapping file [default %default]"),
                        make_option(c("-f", "--fields"),  default=NULL,
                                    action="store", type="character",
                                    help="Fields or categories to test [default %default]"),
                        make_option(c("--otus_key"),  default=NULL,
                                    action="store", type="character",
                                    help="Fields or categories to test [default %default]"),
                        make_option(c("--cv"), default=NULL,
                                    action="store", type="character",
                                    help="CV scheme. [default %default]."),
                        make_option(c("--replicate"),  default=NULL,
                                    action="store", type="character",
                                    help="Fields or categories to test [default %default]"),
                        make_option(c("-r", "--models"),  default=NULL,
                                    action="store", type="character",
                                    help=paste("Regression models to use.",
                                        "It can be pls, mars, nnet, svm_rb, svm_poly, svm_linear,",
                                        "knn, cart, m5, ctree, rf, cubist, and gbm. [default %default]",
                                        "If no modes are specified, it run all the common models: ",
                                        paste(regression, collapse=', '),
                                        sep='\n\t\t')),
                        make_option(c("-o", "--output"), default=NULL,
                                    action="store", type="character",
                                    help="Output file names. [default %default]. It will save pdf and Rdata files."),
                        make_option(c("-c", "--cores"), default=n.cores,
                                    action="store", type="integer",
                                    help="Number of CPU cores [default %default]"),
                        make_option(c("-s", "--split"), default=1,
                                    action="store", type="double",
                                    help=paste("Split a only fraction of data as training set and",
                                        "hold out the rest for final testing. It should be between 0",
                                        "and 1. [default %default].",
                                        sep='\n\t\t')),
                        make_option(c("--category"), default=NULL,
                                    action="store", type="character",
                                    help=paste("Provide a category and a value to extract the samples",
                                        "of that category which has the value. For example,",
                                        "'SITE::nostril,skin' will only use the samples that are collected",
                                        "from nostril and skin.",
                                        sep='\n\t\t')),
                        make_option(c("--numeric"), default=NULL,
                                    action="store", type="character",
                                    help=paste("Similar to the '--category' but applies to numeric meta data",
                                        "For example, 'PH::6,12' will only use the samples with PH between 6 and 12 (not including 6 and 12);",
                                        "'DAYS::,16' will only use the samples with days less than 16. [default %default]",
                                        sep='\n\t\t')),
                        make_option(c("--add_category"), default=NULL,
                                    action="store", type="character",
                                    help="Add the categorical field in metadata as preditors"),
                        make_option(c("--add_numeric"), default=NULL,
                                    action="store", type="character",
                                    help="Add the numeric field in metadata as preditors"),
                        make_option(c("--file"), default=NULL,
                                    action="store", type="character",
                                    help="Add the numeric field in metadata as preditors"),
                        ## make_option(c("--balance"), default=FALSE,
                        ##             action="store_true", type="logical",
                        ##             help="Balance the classes. Only for classification."),
                        make_option(c("--feature_selection"), default=FALSE,
                                    action="store_true", type="logical",
                                    help="Do feature selection with RFE? Only support RF currently."),
                        make_option(c("-v", "--verbose"), default=TRUE,
                                    action="store_true", type="logical",
                                    help="Output running infomation? [default %default]"),
                        make_option(c("-d", "--debug"), default=FALSE,
                                    action="store_true", type="logical",
                                    help="Output running infomation? [default %default]"))

    args <- commandArgs(trailingOnly=T)
    x <- which(args %in% "--file")

    if (length(x) > 0) {
        file.arg <- args[x+1]
        if (file.exists(file.arg)) {
            args <- c(args, scan(file.arg, what='character'))
        } else {
            stop("The args file ", file.arg, " does not exist.")
        }
    }

    opt <- parse_args(OptionParser(usage = "Rscript %prog [options] file.",
                                   description = paste("Example:",
                                       "# Run on date and sex with cubist and random forest models",
                                       "Rscript %prog -f DATE,SEX -r cubist,rf",
                                       "# Run on PH with random forest model and save output rf.Rdata and rf.pdf",
                                       "Rscript %prog -f PH -r rf -o rf",
                                       sep="\n\t"),
                                   option_list = option_list),
                      args=args)
    opt
}

## plot the feature importance to show
## the important taxonomies
plot.imp <- function (imp, tax.16s, topImp=10, ...) {
    x <- imp$importance
    x <- x[order(-x[1]), , drop=F]
    taxId <- rev(gsub("`+", "", rownames(x)[1:topImp]))
    if ( is.null(tax.16s)) {
        plot(imp, top=topImp)
    } else {
        taxImp <- tax.16s[taxId]
        ## this axis function will enable the tax ID to plot on the left side
        ## of y axis and tax string on the right side.
        axis.sigmasq <- function(side, ...) {
            switch(side,
                   left = {
                       panel.axis(side=side, outside=TRUE, text.cex=0.7,
                                  at=c(1:topImp), labels=taxId)
                   },
                   right = {
                       panel.axis(side=side, outside=TRUE, text.cex=0.7,
                                  at=c(1:topImp), labels=taxImp)
                   },
                   axis.default(side=side, ...))
        }

        ## plot top 10 variable importance
        plot(imp, top=topImp, axis=axis.sigmasq, ...)
    }
}


accuracy <- function(model.tuned, metric=c('RMSE', 'Rsquared'), stats=c('mean', 'se')) {
    ## require(caret)
    ## metric should be the column names or column numbers
    se <- function(x) sd(x)/sqrt(length(x))
    accuracy <- apply(model.tuned$resample[, metric, drop=FALSE],
                      2,
                      function (x) {
                          sapply(stats, function(y) get(y)(x))
                      })
    accuracy <- as.data.frame(accuracy)
    accuracy$Model <- model.tuned$method
    # accuracy$Stats <- c('MEAN', 'SE')
    accuracy
}


classification.tune <- function (trainX, trainY, model, ctrl=NULL, idx=NULL, ...) {
    require(caret)
    if (is.null(ctrl)) {
        set.seed(1)
        ctrl <- trainControl(method = "repeatedcv",
                             repeats = 5, number = 10, # 10-fold CV, 5 repeats
                             selectionFunction = "oneSE",
                             summaryFunction = if (is.factor(trainY) & nlevels(trainY) == 2) {
                                 function(...) c(twoClassSummary(...), defaultSummary(...)) } else defaultSummary,
                             classProbs = TRUE,
                             index = idx,
                             savePredictions = TRUE)
    } else if (ctrl == 'loo') {
        ctrl <- trainControl(method = "LOOCV",
                             classProbs = TRUE,
                             savePredictions = TRUE)
    }
    tuned <- tryCatch( {
        if ('pls' == model) {
            cat("\n---- running PLS...\n")
            set.seed(10)
            plsTune <- train(x = trainX,
                             y = trainY,
                             method = "pls",
                             trControl = ctrl,
                             metric = "Kappa",
                             tuneGrid = expand.grid(.ncomp = 1:9),
                             preProc = c("center", "scale"),
                             ...)
            plot(plsTune)
            plsTune
        } else if ('glm'==model) {
            # logistic regression model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "glm",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('lda'==model) {
            # linear discriminant model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "lda",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('glmnet'==model) {
            # glmnet model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "glmnet",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('pam'==model) {
            # nearest shrunken model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "pam",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('fda'==model) {
            # flexible discriminant model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "fda",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('svmRadial'==model) {
            # SVM radial model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "svmRadial",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('knn'==model) {
            # KNN model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "knn",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('nb'==model) {
            # naive baysian model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "nb",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('mda'==model) {
            # mixture discriminant model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "mda",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('sparseLDA'==model) {
            # sparse logistic regression model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "sparseLDA",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('PART'==model) {
            # rule-based model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "PART",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 10)
            plot(partTune)
            partTune
        } else if ('C5.0Rules'==model) {
            # rule-based model

            set.seed(10)
            partTune<- train(x = trainX,
                           y = trainY,
                           method = "C5.0Rules",
                           trControl = ctrl,
                           metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                           tuneLength = 3)
            plot(partTune)
            partTune
        } else if ('rf'==model) {
            mtryGrid <- data.frame(.mtry = floor(seq(10, ncol(trainX), length = 10)))
            set.seed(10)
            rfTune <- train(x = trainX,
                            y = trainY,
                            method = "rf",
                            trControl = ctrl,
                            metric = ifelse(nlevels(trainY) > 2, "Kappa", "ROC"),
                            ntree = 500,
                            tuneGrid = mtryGrid,
                            importance = TRUE,
                            ...)
            plot(rfTune)
            rfTune
        } else if ('gbm'==model) {
            cat("\n---- running boosting tree...\n")
            gbmGrid <- expand.grid(.interaction.depth = seq(1, 7, by = 2),
                                   .n.trees = seq(100, 1000, by = 50),
                                   .shrinkage = c(0.01, 0.1))
            set.seed(10)
            gbmTune <- train(x = trainX,
                             y = trainY,
                             method = "gbm",
                             trControl = ctrl,
                             # metric = if (nlevels(trainY) > 2) "Kappa" else "ROC",
                             metric = "Kappa",
                             tuneGrid = gbmGrid,
                             ## tuneLength = 200,
                             verbose = FALSE,
                             ...)
            plot(gbmTune, auto.key = list(columns = 4, lines = TRUE))
            gbmTune
        }
    }, error=function(err) {
        ## message(paste("Failed running category:", label))
        cat("original error message:\n")
        print(err)
        return (NA)
    } )
    tuned
}


regression.tune <- function (trainX, trainY, model, ctrl=NULL, ...) {
    ## use "within one standard deviation" model
    ## and repeated 10-fold CV
    require(caret)
    if (is.null(ctrl)) {
        set.seed(1)
        ctrl <- trainControl(method="repeatedcv", number=10, repeats=5,
                             savePredictions = TRUE,
                             selectionFunction = "oneSE")
    }

    tuned <- tryCatch( {
        if ('lm' == model) {
            cat("\n---- running Linear regression...\n")
            set.seed(10)
            lmTune <- train(x = trainX,
                            y = trainY,
                            method = "lm",
                            trControl = ctrl)
            lmTune
        } else if ('pls' == model) {
            cat("\n---- running PLS...\n")
            set.seed(10)
            plsTune <- train(x = trainX,
                             y = trainY,
                             method = "pls",
                             trControl = ctrl,
                             tuneGrid = expand.grid(.ncomp = 1:9),
                             ## tuneLength = 12,
                             preProc = c("center", "scale"),
                             ...)
            plot(plsTune)
            plsTune
        } else if ('mars' == model) {
            ## no need for data transformation;
            ## correlated features will confound feature importance.
            cat("\n---- running MARS...\n")
            marsGrid <- expand.grid(.degree = 1:2,
                                    .nprune = c(1:9, seq(10, 100, by=2)))
            set.seed(10)
            marsTune <- train(x = trainX,
                              y = trainY,
                              method = "earth",
                              trControl = ctrl,
                              tuneGrid = marsGrid,
                              ## tuneLength = 100,
                              ...)
            plot(marsTune)
            marsTune
        } else if("nnet" == model) {
            cat("\n---- running neural network...\n")
            nnetGrid <- expand.grid(.decay = c(0, 0.01, .1),
                                    .size = c(1, 3, 5, 7, 9),
                                    .bag = FALSE)
            set.seed(10)
            nnetTune <- train(x = trainX,
                              y = trainY,
                              trControl = ctrl,
                              method = "avNNet",
                              tuneGrid = nnetGrid,
                              ## tuneLength = 100,
                              preProc = c("center", "scale"),
                              linout = TRUE,
                              trace = FALSE,
                              MaxNWts = 9 * (ncol(trainX) + 1) + 9 + 1,
                              allowParallel = FALSE,
                              maxit = 100,
                              ...)
            plot(nnetTune)
            nnetTune
        } else if("svm_rb" == model) {
            cat("\n---- running SVM radial basis...\n")
            set.seed(10)
            svmRGrid <- expand.grid(.C = 2^(-2:5),
                                    .sigma = c(0.1, 0.3, 0.5))
            svmRTune <- train(x = trainX,
                              y = trainY,
                              method = "svmRadial",
                              tuneGrid = svmRGrid,
                              trControl = ctrl,
                              tuneLength = 100,
                              preProc = c("center", "scale"),
                              ...)
            plot(svmRTune, scales = list(x = list(log = 2)))
            svmRTune
        } else if("svm_poly" == model) {
            cat("\n---- running SVM polynomial...\n")
            svmPGrid <- expand.grid(.degree = 1:2,
                                    .scale = c(0.01, 0.005, 0.001),
                                    .C = 2^(-2:5))
            set.seed(10)
            svmPTune <- train(x = trainX,
                              y = trainY,
                              method = "svmPoly",
                              trControl = ctrl,
                              preProc = c("center", "scale"),
                              tuneGrid=svmPGrid,
                              ## tuneLength = 200,
                              ...)
            plot(svmPTune,
                 scales = list(x = list(log = 2), between = list(x = .5, y = 1)))
            svmPTune
        } else if ("svm_linear" == model) {
            cat("\n---- running SVM linear...\n")
            set.seed(10)
            svmLGrid <- expand.grid(.C = 2^(-2:5))
            svmLTune <- train(x = trainX,
                              y = trainY,
                              method = "svmLinear",
                              trControl = ctrl,
                              tuneGrid = svmLGrid,
                              ## tuneLength = 12,
                              preProc = c("center", "scale"),
                              ...)

            plot(svmLTune,
                 scales = list(x = list(log = 2), between = list(x = .5, y = 1)))
            svmLTune
        } else if ("knn" == model)  {
            cat("\n---- running KNN...\n")
            set.seed(10)
            knnTune <- train(x = trainX,
                             y = trainY,
                             method = "knn",
                             trControl = ctrl,
                             tuneGrid = data.frame(.k = 1:20),
                             tuneLength = 5,
                             preProc = c("center", "scale"),
                             ...)
            plot(knnTune)
            knnTune
        } else if ("cart" == model) {
            cat("\n---- running CART...\n")
            library(rpart)

            set.seed(10)
            cartTune <- train(x = trainX,
                              y = trainY,
                              method = "rpart",
                              trControl = ctrl,
                              ## tune the complexity parameter
                              tuneLength = 25,
                              ...)
            plot(cartTune, scales = list(x = list(log = 10)))
            cartTune
        } else if ("ctree" == model) {
            cat("\n---- running conditional inference tree...\n")
            cGrid <- data.frame(.mincriterion = sort(c(.95, seq(.75, .99, length = 2))))

            set.seed(10)
            ctreeTune <- train(x = trainX,
                               y = trainY,
                               method = "ctree",
                               trControl = ctrl,
                               tuneGrid = cGrid,
                               ## tuneLength = 100,
                               ...)
            plot(ctreeTune)
            plot(ctreeTune$finalModel)
            ctreeTune
        } else if ("m5" == model) {
            cat("\n---- running M5...\n")
            set.seed(10)
            m5Tune <- train(x = trainX,
                            y = trainY,
                            method = "M5",
                            trControl = ctrl,
                            control = Weka_control(M = 10),
                            ...)
            plot(m5Tune)
            plot(m5Tune$finalModel)
            m5Tune
        } else if ("gbm" == model) {
            cat("\n---- running boosting tree...\n")
            gbmGrid <- expand.grid(.interaction.depth = seq(1, 7, by = 2),
                                   .n.trees = seq(100, 1000, by = 50),
                                   .shrinkage = c(0.01, 0.1))
            set.seed(10)
            gbmTune <- train(x = trainX,
                             y = trainY,
                             method = "gbm",
                             trControl = ctrl,
                             tuneGrid = gbmGrid,
                             ## tuneLength = 200,
                             verbose = FALSE,
                             ...)
            plot(gbmTune, auto.key = list(columns = 4, lines = TRUE))
            gbmTune
        } else if ("rf" == model) {
            cat("\n---- running random forest...\n")
            n <- ncol(trainX)
            if (n > 20) {
                mtryGrid <- data.frame(.mtry = floor(seq(10, n, length = 10)))
            } else {
                mtryGrid <- data.frame(.mtry = seq(10, n))
            }

            set.seed(10)
            rfTune <- train(x = trainX,
                            y = trainY,
                            method = "rf",
                            trControl = ctrl,
                            tuneGrid = mtryGrid,
                            ntree = 1000,
                            importance = TRUE,
                            ...)
            plot(rfTune)
            print(rfTune)
            rfTune
        } else if ("cubist" == model) {
            cat("\n---- running cubist...\n")
            cbGrid <- expand.grid(.committees = c(1:10, 20, 50, 75, 100),
                                  .neighbors = c(0, 1, 5, 9))

            set.seed(10)
            cubistTune <- train(x = trainX,
                                y = trainY,
                                method = "cubist",
                                trControl = ctrl,
                                tuneGrid = cbGrid,
                                ## tuneLength = 100,
                                ...)
            plot(cubistTune, auto.key = list(columns = 4, lines = TRUE))
            cubistTune
        }

    }, error=function(err) {
        ## message(paste("Failed running category:", label))
        cat("ORIGINAL ERROR MESSAGE:\n")
        print(err)
        return (NA)
    })
    tuned
}


rf.cv <- function(model) {
    ## input is like big.tuned.list$Day$rf
    mtry <- model$bestTune$mtry
    pred <- model$pred
    best.pred <- pred[ pred$mtry==mtry, c('obs', 'pred')]
    best.pred
}


y.yhat.ggplot2 <- function(testResults, title='') {
    ## The testResults is a data.frame that contains observed y as 1st column
    ## and one or more yhat columns
    require(reshape2)
    require(ggplot2)
    obs <- testResults[,1]
    ## random predictions by permutating the obs: repeat for 100 times
    rand = replicate(100, sample(obs, size=length(obs), replace=F))
    rand.rmse = apply(rand, 2, caret::RMSE, obs)
    rand.rmse.mean <- format(round(mean(rand.rmse), 2), nsmall=2)
    rand.rmse.sd <- format(round(sd(rand.rmse), 2), nsmall=2)
    rand.rmse.str <- paste('Rand RMSE', '=', rand.rmse.mean, '\u00b1', rand.rmse.sd)
    rand.r2 = apply(rand, 2, caret::R2, obs)
    rand.r2.mean <- format(round(mean(rand.r2), 2), nsmall=2)
    rand.r2.sd <- format(round(sd(rand.r2), 2), nsmall=2)
    rand.r2.str <- paste('Rand R2', '=', rand.r2.mean, '\u00b1', rand.r2.sd)

    for(i in 2:length(testResults)) {
        pred <- testResults[,i]
        rmse <- round(caret::RMSE(pred, obs), 2)
        rmse.str <- paste('RMSE', '=', rmse)
        r2 <- round(caret::R2(pred, obs), 2)
        r2.str <- paste('R2', '=', r2)
        df <- cbind(testResults[, c(1, i)], random=rand[,i])
        colnames(df)[1] = 'obs'
        df.2 <- melt(df, id = 'obs', value.name='prediction')
        p <- ggplot(df.2, aes(x=obs, y=prediction, color=variable)) +
            geom_point(shape=16, size=3) +
            geom_abline(mapping=aes(slope=1, intercept=0)) +
            ggtitle(paste(title, rmse.str, r2.str, rand.rmse.str, rand.r2.str,
                          sep='\n'))
        print(p)
    }
}

y.yhat <- function(testResults) {
    ## The testResults must contain y as 1st column and one or more yhat columns
    method.names <- names(testResults)
    obs <- testResults[,1]
    ## random predictions by permutating the obs
    rand = replicate(100, sample(obs, size=length(obs), replace=F))
    rand.rmse = apply(rand, 2, caret::RMSE, obs)
    rand.r2 = apply(rand, 2, caret::R2, obs)
    for(i in 2:length(testResults)) {
        pred <- testResults[,i]
        plot(pred ~ obs,
             xlab=method.names[1],
             ylab=method.names[i],
             pch=20)
        ## plot one random permutation result too
        points(x=obs, y=rand[,1], col='blue', pch=20)
        abline(0, 1, col="red")
        ## mtext(paste(c("RMSE=", "R^2="),
        ##             c(RMSE())))
        rmse <- format(round(caret::RMSE(pred, obs), 2), nsmall=2)
        rsq <- format(round(caret::R2(pred, obs), 2), nsmall=2)
        mtext(paste(c("RMSE","R^2 "), c(rmse, rsq), sep='=', collapse='    '),
              line=1)
        rand.rmse.mean <- format(round(mean(rand.rmse), 2), nsmall=2)
        rand.rmse.sd <- format(round(sd(rand.rmse), 2), nsmall=2)
        ## the unicode is for plus/minus symbol
        rand.rmse.str <- paste(rand.rmse.mean, '\u00b1', rand.rmse.sd)
        rand.r2.mean <- format(round(mean(rand.r2), 2), nsmall=2)
        rand.r2.sd <- format(round(sd(rand.r2), 2), nsmall=2)
        rand.r2.str <- paste(rand.r2.mean, '\u00b1', rand.r2.sd)

        mtext(paste(c("RMSE","R^2 "), c(rand.rmse.str, rand.r2.str), sep='=', collapse='    '),
              col='blue')
        ## legend("topleft", text.col="black", "ab",
               ## paste(c("RMSE","R^2 "), c(rmse, rsq), sep='=', collapse='\n'))
    }
}

cm.result <- function(cm, title, table.fp=NULL, reference=NULL) {
    ## cm is the output of confusionMatrix from caret
    cm.table = prop.table(cm$table, 2) * 100

    a = round(sum(diag(cm$table)) / sum(cm$table) * 100, 2)
    ## cat(a, pred.cm$overall['Accuracy'], '\n')
    if (! is.null(table.fp)) {
        write.table(cm.table, table.fp, quote=F, sep='\t')
    }
    ## main = paste(fn, a, random.mean, '+/-', random.sdev, sep=' ')
    if (is.null(reference)) {
        main = paste(title, a)
    } else {
        main = paste(title, a, round(max(table(reference)) * 100 / length(reference), 2), sep=' ')
    }
    bb = as.table(t(cm.table)[,nrow(cm.table):1])
    hm = levelplot(bb, scales=list(x=list(rot=90)),
                   main=main,
                   newpage=T)
    print(hm)
}

diagnostics <- function(trainX, trainY, testX, testY, sizes=NULL, steps=15, repeats=3,
                        model='rf', metrics=c('RMSE', 'Rsquared')) {
    require(caret)
    if (is.null(sizes)) {
        maxSize <- nrow(trainX)
        minSize <- 32
        if ((maxSize - minSize) <= steps) {
            sizes <- minSize:maxSize
        } else {
            sizes <- round(seq(minSize, maxSize, length.out=steps))
        }
    }
    partitions <- sizes / nrow(trainX)
    error.types <- c('Train', 'CV', 'Test')
    labels <- apply(expand.grid(metrics, error.types), 1, paste, collapse='.')
    ## the order of train, cv, test is consistent with what's inside for loop
    error.array <- replicate(repeats, sapply(partitions, function(partition) {
        rows <- createDataPartition(trainY, p=partition, list=F)
        trX <- trainX[rows, ]
        trY <- trainY[rows]
        tuned <- regression.tune(trX, trY, model)

        train.err <- postResample(trY, predict(tuned, trX))[metrics]

        cv.err <- colMeans(tuned$resample[,metrics,drop=FALSE])

        test.err <- postResample(testY, predict(tuned, testX))[metrics]

        x <- c(partition, train.err, cv.err, test.err)
    }))
    ## error.arrays is now a 3-D array
    if (FALSE) save(error.array, file='diagnostic.Rdata')
    dimnames(error.array) <- list(d1=c('Fraction', labels),
                                  d2=paste('Fraction', 1:steps, sep=''),
                                  d3=paste('Repeat', 1:repeats, sep=''))
    if (FALSE) save(error.array, file='diagnostic.Rdata')
    t(as.data.frame(error.array))
}

diagn.plot <- function (diagn, metric) {
    ## This function is closely related to diagnostic function.
    if (class(diagn) != 'data.frame')
        diagn = as.data.frame(diagn)
    if (length(metric) > 1 | mode(metric) != 'character')
        stop('Wrong metric')
    require(ggplot2)
    diagn$Repeat <- gsub('^.*\\.', '', rownames(diagn))
    i <- grep(paste('^', metric, sep=''), colnames(diagn), value=TRUE)
    x <- diagn[, c('Fraction', 'Repeat', i)]
    require(reshape2)
    x <- melt(x, id=c('Fraction', 'Repeat'))
    if (metric=='Rsquared') {
        x.p <- ggplot(x, aes(x=Fraction, y= 1-value,
                             colour=variable, shape=Repeat,
                             group = interaction(variable, Repeat))) +
                                 labs(y = paste('1 -', metric),
                                      x='Fraction',
                                      title='Learning Curve')
    } else {
        x.p <- ggplot(x, aes(x=Fraction, y= value,
                             colour=variable, shape=Repeat,
                             group = interaction(variable, Repeat))) +
                                   labs(y = metric,
                                      x='Fraction',
                                      title='Learning Curve')
    }
    x.p + geom_line() + geom_point(size=3)
}


plot.rf.rocs <- function(models, labels, colors=c('red', 'black'), out='roc.pdf') {
    ## Plot multiple ROC curves on the same plot.
    ## models is a list of models
    ## this only apply to random forest model
    require(caret)
    require(pROC)
    pdf(out)
    for (ii in 1:length(models)) {
        model = models[[ii]]
        pred <- model[['pred']]
        pred.tuned <- pred[ pred[['mtry']] == model[['bestTune']][1,'mtry'], ]
        response <- factor(pred.tuned[['obs']])
        prediction <- pred.tuned[[levels(response)[1]]]
        tuned.roc <- roc(response = response,
                         predictor = prediction)
        labels[ii] <- paste(labels[ii], ' (AUC:', round(tuned.roc$auc[1],3), ')', sep='')
        ## plot(tuned.roc, percent=TRUE)
        if (ii==1) {
            plot.roc(response, prediction,
                     main='ROC', print.thres=seq(0.4, 0.9, 0.1),# print.auc=T,
                     percent=TRUE, col=colors[ii])
        } else {
            lines.roc(response, prediction,
                      percent=TRUE, col=colors[ii], add=T)
        }
    }

    legend("bottomright", legend=labels, col=colors, lwd=2)
    dev.off()
}


opt <- interface()

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

meta <- read.table.meta(opt$metadata, quote='"')

meta.col <- colnames(meta)


if (is.null(opt$fields)) {
    ## stop("No field is provided to do regression on.")
    outcome.col <- names(meta)
    boring <- c("#SampleID",
                "BarcodeSequence",
                "LinkerPrimerSequence",
                "TARGET_SUBFRAGMENT",
                "ASSIGNED_FROM_GEO",
                "EXPERIMENT_CENTER",
                "RUN_PREFIX",
                "TAXON_ID",
                "ILLUMINA_TECHNOLOGY",
                "COMMON_NAME",
                "EXTRACTED_DNA_AVAIL_NOW",
                "SAMPLE_CENTER",
                "STUDY_CENTER",
                "Description")
    outcome.col <- outcome.col[! outcome.col %in% boring]
} else {
    outcome.col <- strsplit(opt$fields, ',')[[1]]
    x <- which(! outcome.col %in% meta.col)
    if (length(x) > 0) {
        stop("Field(s) ", paste(outcome.col[x], collapse=','), " do not exist in meta data")
    }
}

## extract part of the samples by their meta data
if (! is.null(opt$category)) {
    ## e.g. "SITE::nostril,skin:_:SEX::male"
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
    }
}


if (! is.null(opt$numeric)) {
    ## e.g. "PH::6,12:_:TEMP::,32"
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
            n <- n & i > j[1]
        if (! is.na(j[2]))
            n <- n & i < j[2]
        meta <- meta[n, ]
    }
}


otus.2 <- read.table.otus(opt$input_otu_table, col=opt$otus_key, quote='"')
otus <- otus.2$otus
otus.key <- otus.2$col

if (length(otus.key)!=0) {
    tax.16s <- otus.key
    if (opt$otus_key == 'taxonomy') {
        tax.16s <- gsub("^Root; ", "", tax.16s)
        ## insert a newline for every three levels of taxonomy
        tax.16s <- gsub("([^;]*); ([^;]*); ([^;]*); ", '\\1; \\2; \\3\n', tax.16s)
    }
    names(tax.16s) <- colnames(otus)
} else {
    tax.16s <- NULL
}

## remove the 6-digit suffix of the sample IDs in the mapping file.
## meta.sid <- gsub(".[0-9]{6}$", "", as.character(meta[[1]]))

sample.ids <- intersect(rownames(meta), rownames(otus))
meta <- meta[sample.ids, ]
otus <- otus[sample.ids, ]

if (opt$debug) save.image('debug.Rdata')

## add numeric fields as predictors
if (! is.null(opt$add_numeric)) {
    add.pred <- strsplit(opt$add_numeric, ',', fixed=TRUE)[[1]]
    not.in <- which(! add.pred %in% colnames(meta))
    if (length(not.in) > 0) {
        stop(paste(c(add.pred[not.in], "not in the meta data!!!"), collapse=' '))
    }
    to.add <- meta[, add.pred]
    not.numeric <- which(! sapply(to.add, is.numeric))
    if (length(not.numeric) > 0) {
        stop(paste(c(add.pred[not.numeric], "not numeric!!!"), collapse=''))
    }
    otus <- cbind(meta[, add.pred], otus)
    colnames(otus)[1:length(add.pred)] <- add.pred
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
}

if (is.null(opt$output)){
    if (! is.null(opt$file)) {
        output = strsplit(opt$file, '.args')[[1]]
    } else {
        output = 'benchmark'
    }
} else {
    output = opt$output
}

pdf(sprintf("%s.pdf", output))

min.sample.size <- 12
accuracies <- data.frame()
top.features <- data.frame()
big.tuned.list <- list()

replicate <- meta[, opt$replicate]
