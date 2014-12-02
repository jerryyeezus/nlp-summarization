import nltk.data

def create_edus(infilename, outfilename):
  text = open(infilename).read()
  sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = sent_detector.tokenize(text.strip())
  out = open(outfilename, 'w')
  for sentence in sentences:
    out.write(sentence + "\n");

#create_edus("./examples/battery-life_amazon_kindle.txt.data", "./examples/battery-life.edus")