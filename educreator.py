import codecs
import nltk.data

def create_edus(infilename, outfilename):
  text = open(infilename).read() #.decode("ISO-8859-1").encode("UTF-8")
  sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = sent_detector.tokenize(text.strip())
  with codecs.open(outfilename, 'w', encoding="UTF-8") as out:
    for sentence in sentences:
      out.write(sentence + "\n")

create_edus("./topics/battery-life_amazon_kindle.txt.data", "./summary/battery-life.edus")
