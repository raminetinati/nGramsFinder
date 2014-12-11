#Author
import sys
import nltk


def loadFileToSingleDocument(filename):
	singleDocument = ""
	with open(filename, "r") as f:
		for line in f:
			try:
				line.decode('ascii')
			except:
				pass
			else:
				singleDocument = singleDocument+" "+line
	return singleDocument


def saveResultsFromList(results):
	output = open("results_trigrams_raw.csv","w")
	for item in results:
		try:
	 		output.write(str(item)+"\n")
	 	except:
	 		pass
	print len(list(results))
	output.close()

def aggregateListItems(listToAgg):
	listEntryAndCount = {}
	for item_r in listToAgg:
		item = str(item_r)
		print item
		if item in listEntryAndCount:
			cnt = listEntryAndCount[item]+1
			listEntryAndCount[item] = cnt
		else:
			listEntryAndCount[item] = 1

	return listEntryAndCount

def saveResultsFromDict(dictOfResults):
	output = open("results_trigrams_aggregated.tsv","w")
	for k,v in dictOfResults.iteritems():
		output.write(str(k)+"\t"+str(v)+"\n")
	output.close()

def convertGenToList(gen):
	lst = []
	for i in gen:
		lst.append(str(i))
	return lst


#main run module
if __name__ == '__main__':
	#filename = sys.argv[1]
	documentOfWords = loadFileToSingleDocument("textToProcess")
	words = nltk.word_tokenize(documentOfWords)
	trigrams = nltk.trigrams(words)
	trigrams_lst = convertGenToList(trigrams)

	saveResultsFromList(trigrams_lst)

	# for i in trigrams_lst:
	# 	print str(i)

	dictOfResults = aggregateListItems(trigrams_lst)

	saveResultsFromDict(dictOfResults)

	
