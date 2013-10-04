import metaphone

def plausibleWords(incorrectWord):
	
	USengDict = open("enUS.txt","r")
	GBengDict = open("enGB.txt","r")
	phoneticDictUS = open("metaphonicDictUS.txt","r")
	phoneticDictGB = open("metaphonicDictGB.txt","r")
	
	temp = (metaphone.dm(incorrectWord))[0]
	plausibleList = []
	plausibleListTemp = []
	
	ctr = 0
	for line in phoneticDictUS:
		if line[:-1] == temp:
			plausibleListTemp.append((ctr,"USprimary"))
		ctr = ctr + 1
	
	ctr = 0
	for line in phoneticDictGB:
		if line[:-1] == temp:
			plausibleListTemp.append((ctr,"GBprimary"))
		ctr = ctr + 1
	
	linesUS = USengDict.readlines()
	linesGB = GBengDict.readlines()
	
	for i in xrange(len(plausibleListTemp)):
		if plausibleListTemp[i][1] == "USprimary":
			plausibleList.append(linesUS[plausibleListTemp[i][0]][:-1])
		else:
			plausibleList.append(linesGB[plausibleListTemp[i][0]][:-1])
	
	return plausibleList