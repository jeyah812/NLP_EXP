import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [
    "I love natural language processing",
    "It is used in chatbots",
    "The sky is blue"
]

docs = [nlp(sent) for sent in sentences]

print("Sentence Coherence Scores:")
for i in range(len(docs) - 1):
    score = docs[i].similarity(docs[i + 1])
    print(f"Sentence {i+1} → {i+2}: {score}")
