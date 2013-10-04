import nltk

def adjust(lst):
	for i in xrange(len(lst)):
		if lst[i][:-1] == ".":
			lst[i] = lst[i][:-1]
		if lst[i] == "'" or lst[i] == "'s":
			lst[i-1] = lst[i-1] + lst[i]
			print lst[i-1]
	def clr(s):
		if (s[-1] == "'" or s[-2:] == "'s") and ((s != "'") and (s != "'s")):
			return True
		return s.isalnum()
	
	lst = filter(clr,lst)
	return lst

def tokenizer():
	inputString = raw_input("Enter the text to be SpellNazi'ed: ")
	sentenceList = nltk.sent_tokenize(inputString)
	splitSentencesArray = []
	for i in xrange(len(sentenceList)):
		splitSentencesArray.append(adjust(nltk.word_tokenize(sentenceList[i])))

	if splitSentencesArray[len(splitSentencesArray)-1] == []:
		splitSentencesArray = splitSentencesArray[:-1]

	return splitSentencesArray




