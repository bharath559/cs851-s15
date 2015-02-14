d=read.csv("StatusCodes.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data=d[,1]
newData=data[which(data<10)]
png("StatusCodes-histogramNew2.png")
hist(newData,main="StatusCodes Histogram",freq=T,xlab="Status Codes",ylab="Frequency")
dev.off()