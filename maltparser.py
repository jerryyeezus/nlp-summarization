import nltk.parse.malt

parser = nltk.parse.malt.MaltParser(working_dir="./maltparser", mco="engmalt.linear-1.7.mco", additional_java_args=['-Xmx512m'])

def get_head_words(txt):
    graph = parser.raw_parse(txt)
    head_words = []
    head_word_indices = []
    for i in range(1, len(graph.nodelist)):
        head_word_indices.append(graph.nodelist[i]['head'])
        if graph.nodelist[i]['head'] == 0:
            head_words.append(graph.nodelist[i]['word'])
    return head_words, head_word_indices
