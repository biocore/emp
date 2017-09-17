library(caret)
args <- commandArgs(trailingOnly=T)

cat(paste('read in table:', args[1], '\n'))
otus <- read.table.otus(args[1])
save.image('otus.rdata')
tax <- otus$col
x <- otus$otus

nzv <- nearZeroVar(x)
if (length(nzv) > 0) {
    x <- x[, -nzv]
    tax <- tax[-nzv]
}

tooHigh <- findCorrelation(cor(x), .95)
if (length(tooHigh) > 0) {
    x <- x[, -tooHigh]
    tax <- tax[-tooHigh]
}

normalize <- function(df, sum=1000) {
    rs <- rowSums(df)
    zero.sum <- which(rs==0)
    if (length(zero.sum) > 0) {
        df <- df[-zero.sum, ]
        rs <- rs[-zero.sum]
    }
    df * sum / rs
}

x <- normalize(x)
cat(paste('output table:', args[2], '\n'))
write.table.otus(list(otus=x, col=tax), args[2])
