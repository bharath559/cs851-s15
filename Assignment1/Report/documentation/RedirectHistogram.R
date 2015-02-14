d=read.csv("histogramLinkdata.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data=d[,1]
newData=data[which(data<10)]
png("redirect-histogramNew2.png")
hist(newData,main="Redirects Histogram",freq=T,xlab="Redirects",ylab="Frequency",ylim=c(0,20000),xlim=c(0,10))
dev.off()
