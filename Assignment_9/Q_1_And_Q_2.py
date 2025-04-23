import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

text = """Technology has revolutionized the way we live, work, and connect with others. 
From smartphones to artificial intelligence, it continues to shape our daily experiences. 
The internet has made knowledge more accessible than ever before. 
Innovations in robotics and automation are changing industries rapidly. 
While there are concerns about privacy and over-dependence, technology also opens doors to endless possibilities and progress."""

text_lower = text.lower()
text_clean = text_lower.translate(str.maketrans("", "", string.punctuation))


word_tokens = word_tokenize(text_clean)
sentence_tokens = sent_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in word_tokens if word not in stop_words]

fdist = FreqDist(filtered_words)

print("\nSentence Tokens:\n", sentence_tokens)
print("\nFiltered Words:\n", filtered_words)
print("\nTop 10 Frequent Words:")
print(fdist.most_common(10))

fdist.plot(10, title="Top 10 Word Frequencies (Excluding Stopwords)")
plt.show()

#Q2-------------------------------------------------------

from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

# Using the filtered_words from Q1
porter_stemmed = [porter.stem(word) for word in filtered_words]
lancaster_stemmed = [lancaster.stem(word) for word in filtered_words]
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]


print("\nOriginal Filtered Words:\n", filtered_words)
print("\nPorter Stemmer:\n", porter_stemmed)
print("\nLancaster Stemmer:\n", lancaster_stemmed)
print("\nLemmatized Words:\n", lemmatized)
