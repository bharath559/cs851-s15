
B <- c(40, 20.48, 4,15.36)
png("Sizehistogram.png")
barplot(B, main="Average Size Comparision of WARCs", xlab="WARC Generator Tool", ylab="Size in MB", names.arg = c("WAIL", "WARCreate","wget","webrecorder.io"))
dev.off()