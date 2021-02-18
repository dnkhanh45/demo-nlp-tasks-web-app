from pyvi import ViTokenizer, ViPosTagger

def pyvi_prc(text):
    tokens, tags = ViPosTagger.postagging(ViTokenizer.tokenize(text))
    result = {}
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace('_', ' ')
        result[tokens[i]] = tags[i]
    return result

if __name__ == '__main__':
    text = input()
    print(pyvi_prc(text))