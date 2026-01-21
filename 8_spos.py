from collections import defaultdict

corpus = [
    ("time", "NN"), ("flies", "VBZ"),
    ("flies", "NNS"), ("like", "IN"),
    ("like", "VB")
]

prob = defaultdict(dict)

for word, tag in corpus:
    prob[word][tag] = prob[word].get(tag, 0) + 1

def stochastic_tagger(sentence):
    result = []
    for word in sentence.split():
        if word in prob:
            tag = max(prob[word], key=prob[word].get)
        else:
            tag = "NN"
        result.append((word, tag))
    return result

print(stochastic_tagger("time flies like"))