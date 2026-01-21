from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing is fun",
    "Machine learning is used in NLP",
    "NLP is part of artificial intelligence"
]

query = ["NLP"]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

similarity_scores = cosine_similarity(tfidf_matrix, query_vector)

print("TF-IDF Similarity Scores:")
for i, score in enumerate(similarity_scores):
    print(f"Document {i+1}: {score[0]}")
