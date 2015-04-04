


htmlF <- read.table('graphhtml.txt', header=T)
htmlData <- rep(htmlF[,1])

textF<- read.table('graphtext.txt', header=T)
textData <- rep(textF[,1])
xlimit <- c(0,50)
ylimit <- c(400,4000)

plot(htmlData, type='l', col='blue',xlim=xlimit,ylim=ylimit, xlab='Word Rank', ylab='Word Frequency', main='Distribution of terms before boilerplate \nremoval (blue) and after boilerplate removal (red)')

lines(textData, type='o', col='red')
