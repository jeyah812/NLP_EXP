import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Time flies like an arrow"
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

print(tags)