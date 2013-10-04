import unicodedata
import nltk
import enchant
import os
import numpy as np
import itertools

import tokenizer
import metaphone
import plausibleWords
import dictionarySearch
import getngrams
import commonLingoReplacement



splitSentencesArray = tokenizer.tokenizer()
splitSentencesArray = commonLingoReplacement.commonLingoReplacement(splitSentencesArray)
incorrectlySpelled = dictionarySearch.dictionarySearch(splitSentencesArray)
testString = []
correctlySpelled = []
outputSentencesArray = splitSentencesArray
tempfiles = []
tempSum = []

def addTwoArrays(one,two):
	return (one + two)

def ngramInputCreator(testString):
	testStr = ""
	for s in xrange(len(testString)):
		if s != (len(testString) - 1):
			testStr = testStr + testString[s] + ", "
			#testStr1 = testStr1 + testString1[s] + "_"
		else:
			testStr = testStr + testString[s]
			#testStr1 = testStr1 + testString1[s]
	return testStr

for i in xrange(len(incorrectlySpelled)):
	plausibleList = plausibleWords.plausibleWords(splitSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]])
	for j in xrange(len(plausibleList)):
		if incorrectlySpelled[i][1] != 0 and incorrectlySpelled[i][1] != (len(splitSentencesArray[incorrectlySpelled[i][0]]) - 1):
			#testString1.append(outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + plausibleList[j] + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1])
			testString.append(outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + " " + plausibleList[j] + " " + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1])
		elif incorrectlySpelled[i][1] == 0:
			#testString1.append(plausibleList[j] + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1])
			testString.append(plausibleList[j] + " " + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1])
		else:
			#testString1.append(outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + plausibleList[j])
			testString.append(outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + " " + plausibleList[j])
	testString1 = zip(*[iter(testString)]*12)
	if len(testString)%12 != 0:
		residue = testString[(-(len(testString)%12)):]
	else:
		residue = []
	#print residue
	for l in xrange(len(testString1)):
		testStr1 = map(ngramInputCreator,testString1)
	if residue != []:
		testStr1.append(ngramInputCreator(residue))
	for l in xrange(len(testStr1)):
		#print testStr1[l]
		getngrams.runQuery(testStr1[l],str(l+1)+".tsv")
		tempfiles.append(open("%s.tsv"%(str(l+1)),"r"))
	for m in xrange(len(testStr1)):
		k = 0
		tempSum1 = [0.0]*len(testStr1[m].split(",")) 
		for lineses in tempfiles[m]:
			if k == 0:
				k = k + 1
				continue
			else:
				#print tempSum1
				#print map(float,lineses.split("\t")[1:])
				tempSum1 = map(addTwoArrays,tempSum1,map(float,lineses.split("\t")[1:]))
				k = k + 1
		tempSum.append(tempSum1)
	tempSum = list(itertools.chain.from_iterable(tempSum))
	'''for m in xrange(len(testStr1)):
		tempfiles[m].close()
		os.remove("%s.tsv"%(str(m+1)))'''
	tempMax = max(tempSum)
	if tempMax == 0:
		correctlySpelled.append("")
	else:
		tempIndex = tempSum.index(tempMax)
		correctlySpelled.append(plausibleList[tempIndex])
	testString = []
	tempfiles = []
	tempSum = []
	
for i in xrange(len(splitSentencesArray)):
	for j in xrange(len(splitSentencesArray[i])):
		try:
			temp = correctlySpelled[incorrectlySpelled.index((i,j))]
			if temp != "":
				outputSentencesArray[i][j] = temp
		except ValueError:
			continue

print outputSentencesArray
				
	
		
			
		

