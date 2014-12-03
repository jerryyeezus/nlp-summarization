from nltk.tag.stanford import POSTagger

postagger = POSTagger("./stanford-postagger-full-2014-10-26/models/english-bidirectional-distsim.tagger",
		"./stanford-postagger-full-2014-10-26/stanford-postagger.jar")
print postagger.tag('What is the airspeed of an unladen swallow ?'.split())
