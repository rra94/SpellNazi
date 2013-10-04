def commonLingoReplacement(inputArray):
	
	#lingoDict = open("commonlingo.tsv","r")
	#linesLingo = lingoDict.readlines()
	a={'1': 'one',
'2': 'two',
'3': 'three',
'4': 'four',
'5': 'five',
'6': 'six',
'7': 'seven',
'8': 'eight',
'9': 'nine',
'10': 'ten',
'd': 'the',
'i': 'I',
'r': 'are',
'c': 'see',
'b': 'be',
'ur': 'your',
'u': 'you',
'o': 'owe',
'ppl': 'people',
'gr8': 'great',
'f9': 'fine',
'2moro': 'tomorrow',
'2night': 'tonight',
'l8r': 'later',
'thx': 'thanks',
'tx': 'thanks',
'thks': 'thanks',
'plz': 'please',
'der': 'there',
'den': 'then',
'ballz': 'balls',
'hathi': 'elephant',
'mins': 'minutes',
'hr': 'hour',
'hrs': 'hours',
'min': 'minute',
'thnx': 'thanks',
'nyt': 'night',
'ni8': 'night',
'ly8': 'lite',
'dat': 'that',
'kul': 'cool',
'bcoz': 'because'}
	for i in xrange(len(inputArray)):
		for j in xrange(len(inputArray[i])):
			if inputArray[i][j] in a.keys():
				inputArray[i][j] = a[inputArray[i][j]]

	return inputArray
