import nltk.parse.malt

def get_head_words(txt):
	parser = nltk.parse.malt.MaltParser(working_dir="./maltparser",
		mco="engmalt.linear-1.7.mco",
		additional_java_args=['-Xmx512m'])
	graph = parser.raw_parse(txt)
	head_words = []
	for i in range(1, len(graph.nodelist)):
		if graph.nodelist[i]['head'] == 0:
			head_words.append(graph.nodelist[i]['word'])
	return head_words
	
#print get_head_words("Until his arms ached, Tom scrubbed")
#print get_head_words("Sitting down, I am euphoric")
