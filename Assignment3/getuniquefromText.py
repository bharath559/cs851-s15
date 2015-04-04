import os, sys
page = ''
wordFrequencyDict = {}
try:
	inputFile = open('total.txt', 'r')
	page = inputFile.read()
	inputFile.close()
except:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(fname, exc_tb.tb_lineno, sys.exc_info() )

tokens = page.split(' ')
for t in tokens:
	wordFrequencyDict.setdefault(t, 0)
	wordFrequencyDict[t] = wordFrequencyDict[t] + 1
wordFrequencyDict = sorted(wordFrequencyDict.items(), key=lambda x:x[1], reverse=True)

totalWords = 0
for tup in wordFrequencyDict:
	totalWords = tup[1] + totalWords

print 'totalWords:', totalWords
print 'totalUniqueWords:', len(wordFrequencyDict)
