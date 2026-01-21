import spacy

nlp = spacy.load("en_core_web_sm")

text = "John went to the store. He bought milk."
doc = nlp(text)

last_noun = None

print("Reference Resolution:")
for token in doc:
    if token.pos_ == "PROPN":
        last_noun = token.text
    if token.pos_ == "PRON":
        print(f"Pronoun '{token.text}' refers to '{last_noun}'")
