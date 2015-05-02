
library(RColorBrewer)
data <- read.table("UnigramJackardDistance.txt")
finalData = rep(data[,1])
title <- "CDF of Unigram Change"
xlab <- "Jaccard Distance"
ylab <- "Probability"
png("unigrams.png")
set.seed(1)
mp <- plot(finalData, type="l", col="red", main=title, xlab=xlab, ylab=ylab, yaxt="n")
