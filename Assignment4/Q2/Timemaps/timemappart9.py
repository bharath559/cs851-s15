# -*- coding: utf-8 -*-
#!/usr/bin/env python
from getConfig import getConfigParameters
import commands
import time
import datetime
import sys
import argparse, os
import subprocess
import hashlib
import tldextract
import urlparse
import glob
import json
import requests


globalMementoUrlDateTimeDelimeter = "*+*+*"

def getMementosPages(url):

	pages = []
	url = url.strip()
	if(len(url)>0):

		firstChoiceAggregator = getConfigParameters('mementoAggregator')
		timemapPrefix = firstChoiceAggregator + url
		#timemapPrefix = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + url

		'''
			The CS memento aggregator payload format:
				[memento, ..., memento, timemap1]; timemap1 points to next page
			The LANL memento aggregator payload format:
				1. [timemap1, ..., timemapN]; timemapX points to mementos list
				2. [memento1, ..., mementoN]; for small payloads
			For LANL Aggregator: The reason the link format is used after retrieving the payload
								 with json format is due to the fact that the underlying code is based
								 on the link format structure. json format was not always the norm 
		'''



		#select an aggregator - start
		aggregatorSelector = ''

		co = 'curl --silent -I ' + timemapPrefix
		head = commands.getoutput(co)

		indexOfFirstNewLine = head.find('\n')
		if( indexOfFirstNewLine > -1 ):

			if( head[:indexOfFirstNewLine].split(' ')[1] != '200' ):
				firstChoiceAggregator = getConfigParameters('latentMementoAggregator')
				timemapPrefix = firstChoiceAggregator + url

		if( firstChoiceAggregator.find('cs.odu.edu') > -1 ):
			aggregatorSelector = 'CS'
		else:
			aggregatorSelector = 'LANL'

		print '...using aggregator:', aggregatorSelector
		#select an aggregator - end

		#CS aggregator
		if( aggregatorSelector == 'CS' ):
			while( True ):
				#old: co = 'curl --silent ' + timemapPrefix
				#old: page = commands.getoutput(co)

				
				page = ''
				r = requests.get(timemapPrefix)
				print 'status code:', r.status_code
				if( r.status_code == 200 ):
					page = r.text

				pages.append(page)
				indexOfRelTimemapMarker = page.rfind('>;rel="timemap"')

				if( indexOfRelTimemapMarker == -1 ):
					break
				else:
					#retrieve next timemap for next page of mementos e.g retrieve url from <http://mementoproxy.cs.odu.edu/aggr/timemap/link/10001/http://www.cnn.com>;rel="timemap"
					i = indexOfRelTimemapMarker -1
					timemapPrefix = ''
					while( i > -1 ):
						if(page[i] != '<'):
							timemapPrefix = page[i] + timemapPrefix
						else:
							break
						i = i - 1
		else:
			#LANL Aggregator
			#old: co = 'curl --silent ' + timemapPrefix
			#old: page = commands.getoutput(co)

			page = ''
			r = requests.get(timemapPrefix)
			if( r.status_code == 200 ):
				page = r.text

			try:
				payload = json.loads(page)

				if 'timemap_index' in payload:

					for timemap in payload['timemap_index']:
						
						timemapLink = timemap['uri'].replace('/timemap/json/', '/timemap/link/')
						#old: co = 'curl --silent ' + timemapLink
						#old: page = commands.getoutput(co)
						#old: pages.append(page)
						r = requests.get(timemapLink)
						if( r.status_code == 200 ):
							pages.append(r.text)
					
				elif 'mementos' in payload:
					#untested block
					timemapLink = payload['timemap_uri']['json_format'].replace('/timemap/json/', '/timemap/link/')
					#old: co = 'curl --silent ' + timemapLink
					#old: page = commands.getoutput(co)
					#old: pages.append(page)

					print 'timemap:', timemapLink
					r = requests.get(timemapLink)
					if( r.status_code == 200 ):
						pages.append(r.text)
					
				
				
			except:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(fname, exc_tb.tb_lineno, sys.exc_info() )

			
			
	return pages


def getItemGivenSignature(page):

	listOfItems = []
	if( len(page) > 0 ):
		page = page.splitlines()
		for line in page:
			if(line.find('memento";') != -1):
				#uriRelDateTime: ['<http://www.webcitation.org/64ta04WpM>', ' rel="first memento"', ' datetime="Mon, 23 Jan 2012 02:01:29 GMT",']
				uriRelDateTime = line.split(';')
				if( len(uriRelDateTime) > 2 ):
					if( uriRelDateTime[0].find('://') != -1 ):
						if( uriRelDateTime[2].find('datetime="') != -1 ):


							uri = ''
							uri = uriRelDateTime[0].split('<')
							#print uri
							if( len(uri) > 1 ):
								uri = uri[1].replace('>', '')
								uri = uri.strip()

							datetime = ''
							datetime = uriRelDateTime[2].split('"')
							if( len(datetime) > 1 ):
								datetime = datetime[1]
							
							if( len(uri) != 0 and len(datetime) != 0 ):
								#print uri, '---', datetime
								listOfItems.append(uri + globalMementoUrlDateTimeDelimeter + datetime)

	return listOfItems

fh = open('part9.txt','r+')
saveFile1 = open("memontoscount9.txt",'w')
count = 0
l = 8000
count1 = 1
for line in fh:
	data = json.loads(line)
	count = 0
	url = data['finalurl']
	pages = getMementosPages(url)
	saveFile = open("memontos"+str(l)+".txt",'w')
	for i in range(0,len(pages)):
		mementos = getItemGivenSignature(pages[i])
		print mementos
		count += len(mementos)
		saveFile.write(str(mementos) + '\n')
	print 'total count of mementos:', count
	saveFile1 = open("count.txt",'a')
	saveFile1.write(str(count) + '\n')
	saveFile1.close()
	l=l+1
	count1 = count1 + 1
	count = 0