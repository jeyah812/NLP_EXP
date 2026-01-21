from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "fairness", "easily"]

for w in words:
    print(ps.stem(w))