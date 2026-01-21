import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "The cat on the roof, purring softly, which belongs to my neighbor, caught a mouse."

# Process sentence
doc = nlp(sentence)

# Token details
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}")

# Prepositional phrases (simple heuristic: chunk containing 'on', 'in', 'at', etc.)
prepositional_phrases = [
    chunk.text
    for chunk in doc.noun_chunks
    if any(token.text.lower() in ["on", "in", "at", "to", "with", "from"] for token in chunk)
]

print("\nPrepositional Phrases:")
print(prepositional_phrases)

# Gerundive phrases (verb ending with 'ing' inside noun chunks)
gerundive_phrases = [
    chunk.text
    for chunk in doc.noun_chunks
    if any(token.text.endswith("ing") for token in chunk)
]

print("\nGerundive Phrases:")
print(gerundive_phrases)

# Infinitive clauses (to + verb → xcomp)
infinitive_clauses = [
    token.text
    for token in doc
    if token.dep_ == "xcomp"
]

print("\nNon-finite Clauses (Infinitive Clauses):")
print(infinitive_clauses)

# Relative clauses (which, that, who → relcl)
relative_clauses = [
    token.text
    for token in doc
    if token.dep_ == "relcl"
]

print("\nRelative Clauses:")
print(relative_clauses)
