from textblob import TextBlob, Word
import timeit


class textblob_text_result:
    def __init__(self, doc, lemmas, sentiment_result):
        self.doc = doc
        self.lemmas = lemmas
        self.sentiment_result = sentiment_result


def get_pos_code(tag):
    if tag[0] == 'N':
        return 'n'
    elif tag[0] == 'V':
        return 'v'
    elif tag[0] == 'J':
        return 'a'
    elif tag[0] == 'R':
        return 'r'
    else:
        return 'n'


def textblob_prc(text):
    doc = TextBlob(text)

    lemmas = {}
    for word in doc.pos_tags:
        w = Word(word[0])
        lemmas[word[0]] = w.lemmatize(get_pos_code(word[1]))

    plr = doc.sentiment.polarity
    if plr < -0.05:
        sentiment_result = 'negative'
    elif plr > 0.05:
        sentiment_result = 'positive'
    else:
        sentiment_result = 'neutral'

    return textblob_text_result(doc, lemmas, sentiment_result)


if __name__ == '__main__':
    text = 'using these methods a text that has been translated into two or more languages may be utilized in combination to provide a more accurate translation into a third language compared with if just one of those source languages were used alone'
    a = textblob_prc(text)
    print(a.lemmas)
    print(a.sentiment_result)
