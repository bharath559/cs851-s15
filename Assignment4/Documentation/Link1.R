
library(RColorBrewer)

data <- read.table('UnigramJackardDistance20', sep=" ",colClasses=c("POSIXct", "numeric"))

title <- "Relative Change in Jaccard Distance through Time"
xlab <- "Date"
ylab <- "Jaccard Distance"

png('url20.png')
par(mar=c(4,4,2.5,2) + 0.1)
set.seed(1)

p1 <- plot(data, type="o", col='red', main=title, xlab=xlab, ylab=ylab, xaxt="n", ylim=c(0,1))

axis.POSIXct(side=1, data$V1, format="%Y-%m-%d")