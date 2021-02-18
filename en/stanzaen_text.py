import stanza

ennlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment,ner,pos,lemma')

def stanzaen_prc(text):
    doc = ennlp(text)
    nes = {}
    for sent in doc.sentences:
        for ent in sent.ents:
            key = ent.type
            if key not in nes:
                nes[key] = []
            nes[key].append(ent.text)
    ner_text = []
    for key, value in nes.items():
        a = ''
        a += key + ': '
        value_len = len(value)
        for index, x in enumerate(value):
            a += x
            if index != value_len - 1:
                a += ", "
        ner_text.append(a)

    return doc, ner_text

if __name__ == '__main__':
    doc, ner_text = stanzaen_prc('Barack Obama was born in Hawaii.')
    print(ner_text)