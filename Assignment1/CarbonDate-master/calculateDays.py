
import sys
import time
import datetime
import json
import statistics
from scipy import stats
def cd(cdate):
    try:
        ct = time.strptime(cdate, "%Y-%m-%dT%H:%M:%S")
        cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
        now = datetime.datetime.now()
        days = (now - cdt).days
        
    except ValueError:
        print ValueError
    return str(days)
def cdtwitter(cdate):
    try:
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(cdate,'%a %b %d %H:%M:%S +0000 %Y'))
        ct = time.strptime(ts, "%Y-%m-%d %H:%M:%S")
        cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
        now = datetime.datetime.now()
        days = (now - cdt).days
    except ValueError:
        print ValueError
    return str(days)
fh=open('carbondateoutputs1','r')
finalStat=open('finalstatistics','w')
finalStatus=open('finalstatisticstxt.txt','w')
finalData = set()
i=0
totalData={}
for line in fh:
    eachJson=json.loads(line)
    if len(eachJson['tweetcreatedDate'])!=0:
         twitterAge = cdtwitter(eachJson['tweetcreatedDate'])
    if eachJson['createdDate']!="":
         linkage = cd(eachJson['createdDate'])
    absValue= abs(int(twitterAge) - int(linkage))
    finalData.add(absValue)
    finalStatus.write(str(absValue)+ '\n')
    sortedlist = sorted(finalData)
print statistics.mean(sortedlist)
print statistics.median(sortedlist)
totalData['data'] = sortedlist
totalData['mean'] =  statistics.mean(sortedlist)
totalData['median'] = statistics.median(sortedlist)
totalData['Std Dev'] = statistics.stdev(sortedlist)
totalData['Std Err']  = stats.sem(sortedlist);
finalStat.write(json.dumps(totalData))
#print statistics.mode(sortedlist) 
fh.close()