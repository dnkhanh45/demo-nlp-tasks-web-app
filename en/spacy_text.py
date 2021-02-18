import spacy
from spacy import displacy

eng = spacy.load('en_core_web_md')

class spacy_text_result:
    def __init__(self, doc, deps, ent):
        self.doc = doc
        self.deps = deps
        self.ent = ent

def spacy_prc(text):
    doc = eng(text)
    for ent in doc.ents:
        ent.merge()

    deps = []
    options = {"compact": True, "bg": "#92A8D1", "color": "black", "font": "Source Sans Pro"}
    for sent in doc.sents:
        deps.append(
            displacy.render(doc[sent.start:sent.end], style="dep", page=True, minify=True, options=options))
    if len(doc.ents) > 0:
        ent = displacy.render(doc, style="ent", page=True, minify=True)
    else:
        ent = text

    return spacy_text_result(doc, deps, ent)

if __name__ == '__main__':
    a = spacy_prc("""Hello it is London""")
    print(a.ent)