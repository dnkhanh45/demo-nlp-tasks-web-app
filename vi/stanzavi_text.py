import stanza

vinlp = stanza.Pipeline(lang='vi', processors='tokenize,pos')

def stanzavi_prc(text):
    doc = vinlp(text)
    return doc
if __name__ == '__main__':
    text = input()
    a = stanzavi_prc(text)
    for sentence in a.sentences:
        for word in sentence.words:
            print(word.text, ",", word.upos, ",", word.xpos)