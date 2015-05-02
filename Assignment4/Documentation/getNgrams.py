from nltk.util import ngrams
import json
import sys
import os
import string

def jaccardDistance(list1, list2):
    union = set(list1).union(list2)
    intersect = set(list1).intersection(list2)
    dist = (len(union) - len(intersect)) * 1.0 / len(union)
    return dist
    
def wordsFromFile(filePath):
    text = ''
    print filePath
    with open(filePath, 'r') as textFile:
        for line in textFile:
            text = text + extractWords(line).strip() + ' '
    words = text.strip().split(' ')
    if '' in words:
        words.remove('')
    return words
def calculateNgrams():
    finalGrams = ngrams(sentence.split(), n)
    for grams in finalGrams:
      print grams

def extractWords(s):
    valid_characters = string.ascii_letters
    valid_following_character = "'-"
    letters = []
    for letter in s:
        if letter in valid_characters:
            letters.append(letter)
        elif len(letters) > 0 and \
            letter in valid_following_character and \
            letters[-1] in valid_characters:
            letters.append(letter)
        elif len(letters) > 0 and letters[-1] != ' ':
            letters.append(' ')
    return ''.join(letters)

mementosDir = 'Texts'
mementosDir2 ='Texts2'
outputfile = open('DifferenceUrl', 'w')
outputfile1 = open('UnigramJackardDistance', 'w')
outputfile2 = open('BigramJackardDistance', 'w')
outputfile3 = open('TrigramJackardDistance', 'w')
filesList = os.listdir(mementosDir)
filesList2 = os.listdir(mementosDir2)
for item in filesList:
    if item in filesList2:
        path1 = mementosDir+'/'+item
        path2 = mementosDir2+'/'+item
        words1 = wordsFromFile(path1)
        words2 = wordsFromFile(path2)
        words1.sort()
        words2.sort()
        bigrams1 = []
        bigrams2 = []
        trigrams1 = []
        trigrams2 = []
        for i in range(0,len(words1)):
            if i >= 1:
                bigrams1.append(words1[i-1] + ' ' + words1[i])
            if i >= 2:
                trigrams1.append(words1[i-2] + ' ' + words1[i-1] + ' ' + words1[i])
        for i in range(0,len(words2)):
            if i >= 1:
                bigrams2.append(words2[i-1] + ' ' + words2[i])
            if i >= 2:
                trigrams2.append(words2[i-2] + ' ' + words2[i-1] + ' ' + words2[i])
        jacadDistanceUni = jaccardDistance(words1,words2)
        jacadDistanceUni2 = jaccardDistance(bigrams1,bigrams2)
        jacadDistanceUni3 = jaccardDistance(trigrams1,trigrams2)
        outputfile1.write(str(jacadDistanceUni)+ '\n')
        outputfile2.write(str(jacadDistanceUni2)+ '\n')
        outputfile3.write(str(jacadDistanceUni3)+ '\n')
    else:
        outputfile.write(item+ '\n')

