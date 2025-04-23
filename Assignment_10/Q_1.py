import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

document = """Nature offers a profound sense of peace and inspiration to those who embrace it. 
Forests whisper ancient secrets, rivers flow with gentle determination, 
and mountains stand as timeless guardians of the earth. 
The changing seasons remind us of life's cycles and the beauty of transformation. 
Even amidst challenges, nature remains a source of healing, strength, and wonder."""

document_lower = document.lower()
document_clean = document_lower.translate(str.maketrans("", "", string.punctuation))

tokens_words = word_tokenize(document_clean)
tokens_sentences = sent_tokenize(document)

english_stopwords = set(stopwords.words('english'))
keywords = [token for token in tokens_words if token not in english_stopwords]

word_frequency = FreqDist(keywords)

print("\nSentence Tokens:\n", tokens_sentences)
print("\nFiltered Keywords:\n", keywords)
print("\nTop 10 Frequent Words:")
print(word_frequency.most_common(10))

word_frequency.plot(10, title="Top 10 Word Frequencies (No Stopwords)")
plt.show()

from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

porter_results = [porter_stemmer.stem(word) for word in keywords]
lancaster_results = [lancaster_stemmer.stem(word) for word in keywords]
lemmatized_results = [wordnet_lemmatizer.lemmatize(word) for word in keywords]

print("\nOriginal Keywords:\n", keywords)
print("\nPorter Stemmer Results:\n", porter_results)
print("\nLancaster Stemmer Results:\n", lancaster_results)
print("\nLemmatized Words:\n", lemmatized_results)
