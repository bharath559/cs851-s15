inputFile=read.csv("finalstatisticstxt.txt",stringsAsFactors=F,header=FALSE,sep="\t")
inputFile
data=inputFile[,1]
output <- function(data) sd(data)/sqrt(length(data))
output(data)