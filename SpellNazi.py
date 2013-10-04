import unicodedata
import nltk
import enchant
import os

import tokenizer
import metaphone
import plausibleWords
import dictionarySearch
import getngrams

splitSentencesArray = tokenizer.tokenizer()
incorrectlySpelled = dictionarySearch.dictionarySearch(splitSentencesArray)
correctlySpelled = []
summationArray = []
outputSentencesArray = splitSentencesArray
tempSum = 0.0

for i in xrange(len(incorrectlySpelled)):
	plausibleList = plausibleWords.plausibleWords(splitSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]])
	for j in xrange(len(plausibleList)):
		if incorrectlySpelled[i][1] != 0 and incorrectlySpelled[i][1] != (len(splitSentencesArray[incorrectlySpelled[i][0]]) - 1):
			testString1 = outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + plausibleList[j] + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1]
			testString = outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + " " + plausibleList[j] + " " + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1]
		elif incorrectlySpelled[i][1] == 0:
			testString1 = plausibleList[j] + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1]
			testString = plausibleList[j] + " " + outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]+1]
		else:
			testString1 = outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + plausibleList[j]
			testString = outputSentencesArray[incorrectlySpelled[i][0]][incorrectlySpelled[i][1]-1] + " " + plausibleList[j]
		os.system("getngrams.py " + testString + " -noprint -quit")
		tempfile = open("%s.tsv" %testString1,"r")
		k = 0
		for lineses in tempfile:
			if k == 0:
				k = k + 1
				continue
			else:
				tempSum = tempSum + float(lineses[(lineses.find("\t")+1):-1])
				k = k + 1
		summationArray.append(tempSum)
		tempSum = 0.0
		tempfile.close()
		os.remove("%s.tsv" %testString1)
	tempMax = max(summationArray)
	if tempMax == 0:
		correctlySpelled.append("")
	else:
		tempIndex = summationArray.index(tempMax)
		correctlySpelled.append(plausibleList[tempIndex])
	summationArray = []
	
for i in xrange(len(splitSentencesArray)):
	for j in xrange(len(splitSentencesArray[i])):
		try:
			temp = correctlySpelled[incorrectlySpelled.index((i,j))]
			if temp != "":
				outputSentencesArray[i][j] = temp
		except ValueError:
			continue

print outputSentencesArray
				
	
		
			
		

