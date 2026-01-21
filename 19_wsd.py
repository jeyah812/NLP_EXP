import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

sentence = "I went to the bank to deposit money"
sense = lesk(word_tokenize(sentence), "bank")

print("Disambiguated Sense:")
print(sense.name())
print(sense.definition())
