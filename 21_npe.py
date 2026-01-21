import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "The intelligent student solved the difficult problem"
doc = nlp(sentence)

print("Noun Phrases:")
for chunk in doc.noun_chunks:
    print(chunk.text)
