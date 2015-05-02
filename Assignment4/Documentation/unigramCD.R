
library(RColorBrewer)
data <- read.table("TrigramJackardDistance.txt")
finalData = rep(data[,1])
title <- "CDF of Change in Unigrams"
xlab <- "Jaccard Distance"
ylab <- "Probability"
png("Trigramq1.png")
par(mar=c(4,4,2.5,2) + 0.1)
set.seed(1)
mp <- plot(finalData, 1:length(finalData), type="l", col="red", main=title, xlab=xlab, ylab=ylab, yaxt="n")
axis(side=2, at=seq(1,2735,length.out=5), labels=seq(0.2,1,by=0.2))