from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

sentence1 = "Cloud computing enables on-demand access to resources."
sentence2 = "Edge computing processes data close to the source."

sentence1_clean = sentence1.translate(str.maketrans('', '', string.punctuation)).lower()
sentence2_clean = sentence2.translate(str.maketrans('', '', string.punctuation)).lower()

tokens1 = sentence1_clean.split()
tokens2 = sentence2_clean.split()

set_tokens1 = set(tokens1)
set_tokens2 = set(tokens2)

shared_words = set_tokens1.intersection(set_tokens2)
total_words = set_tokens1.union(set_tokens2)
jaccard_score = len(shared_words) / len(total_words)

print("Jaccard Similarity:", jaccard_score)

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([sentence1, sentence2])
cosine_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Cosine Similarity:", cosine_score[0][0])

if cosine_score[0][0] > jaccard_score:
    print("Cosine similarity shows better semantic overlap between texts.")
else:
    print("Jaccard similarity shows better common word overlap between texts.")
