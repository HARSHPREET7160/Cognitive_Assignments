from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

review1 = "This laptop is lightweight and fast."
review2 = "Battery performance is disappointing."
review3 = "Crystal clear screen and great audio output."

reviews = [review1, review2, review3]

vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(reviews)
print("BOW Words:", vectorizer.get_feature_names_out())
print("BOW Matrix:\n", bag_of_words.toarray())

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(reviews)

terms = tfidf_vectorizer.get_feature_names_out()
for i in range(len(reviews)):
    row = tfidf_matrix[i].toarray()[0]
    top_indices = row.argsort()[-3:][::-1]
    top_keywords = []
    for idx in top_indices:
        top_keywords.append(terms[idx])
    print("Top TF-IDF Words:", top_keywords)
