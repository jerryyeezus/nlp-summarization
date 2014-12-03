import nltk

def get_head_indices(txt):
	parser = nltk.parse.malt.MaltParser(working_dir="./maltparser",
		mco="engmalt.linear-1.7.mco",
		additional_java_args=['-Xmx512m'])
	graph = parser.raw_parse(txt)
	indices = []
	print graph.nodelist
	correction_factor = 0;
	for i in range(1, len(graph.nodelist)):
		indices.append(graph.nodelist[i]['head'])
	return indices
	
print get_head_indices("Until his arms ached, Tom scrubbed")
print get_head_indices("Sitting down, I am euphoric")
