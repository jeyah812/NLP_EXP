import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

word = "bank"
synsets = wn.synsets(word)

print("Synsets and meanings:")
for s in synsets:
    print(s.name(), ":", s.definition())
