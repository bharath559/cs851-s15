

library(RColorBrewer)

data <- read.table("count.txt",header=FALSE)
finalData = rep(data[,1])
title <- "CDF of Number of Mementos per URI"
xlab <- "Number of Mementos"
ylab <- "Probability"
P1 = ecdf(finalData)
png("memento_counts.png")

p1 <- plot(P1,col="red", main=title, xlab=xlab, ylab=ylab)
