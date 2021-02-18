import nltk
from nltk import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import timeit
class nltk_text_result:
    def __init__(self, pos_tags, lemmas, sentiment_result):
        self.pos_tags = pos_tags
        self.lemmas = lemmas
        self.sentiment_result = sentiment_result

lemmatizer = WordNetLemmatizer()
sentiment_analyzer = SentimentIntensityAnalyzer()

def wordnet_pos_code(tag):
    if tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def nltk_prc(text):
    token_text = word_tokenize(text)
    pos_tags = nltk.pos_tag(token_text)

    lemmas = {}
    for tag in pos_tags:
        lemmas[tag] = lemmatizer.lemmatize(tag[0], pos=wordnet_pos_code(tag[1]))

    sentiment_result = sentiment_analyzer.polarity_scores(text)

    return nltk_text_result(pos_tags, lemmas, sentiment_result)
if __name__ == '__main__':
    text = 'By 1998, "for as little as $29.95" one could "buy a program for translating in one direction between English and a major European language of your choice" to run on a PC. MT on the web started with SYSTRAN offering free translation of small texts (1996) and then providing this via AltaVista Babelfish, which racked up 500,000 requests a day (1997).'
    start = timeit.default_timer()
    a = nltk_prc(text)
    stop = timeit.default_timer()
    print(a.pos_tags)
    print(len(text.split(' ')))
    print(stop - start)