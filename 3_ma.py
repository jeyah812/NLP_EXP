from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["cars", "wolves", "running"]

for w in words:
    print(ps.stem(w))
