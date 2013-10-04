import enchant
dUS = enchant.Dict("en_US")
dGB = enchant.Dict("en_GB")
def dictionarySearch(wordlist):
	incorrectlySpelled = []
	for i in xrange(len(wordlist)):
		for j in xrange(len(wordlist[i])):
			if dUS.check(wordlist[i][j]) == False and dGB.check(wordlist[i][j]) == False:
				incorrectlySpelled.append((i,j))
	return incorrectlySpelled
