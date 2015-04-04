import json
import string
import subprocess
import time
f = open('statusoutputs1','r+')
i=1
for line in f:
	data = json.loads(line)
	link = str(i) + '.html'
	subprocess.Popen(['wget','--output-document',link,str(data['finalurl'])])
	i=i+1
			