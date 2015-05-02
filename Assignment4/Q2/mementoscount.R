

library(RColorBrewer)

myData <- read.table("count.txt")
fullData = rep(myData[,1])

title <- "CDF of Number of Mementos per URI"
xlab <- "Number of Mementos"
ylab <- "Probability"

pdf("memento_counts.pdf", height=4.0, width=4.5)
par(mar=c(4,4,2.5,2) + 0.1)
set.seed(1)
mp <- plot(fullData, 1:length(fullData), type="l", col="red", main=title, xlab=xlab, ylab=ylab, yaxt="n")
axis(side=2, at=seq(1,2735,length.out=5), labels=seq(0.2,1,by=0.2))
