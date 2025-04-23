import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

text = """Nature offers a profound sense of peace and inspiration to those who embrace it. 
Forests whisper ancient secrets, rivers flow with gentle determination, 
and mountains stand as timeless guardians of the earth. 
The changing seasons remind us of life's cycles and the beauty of transformation. 
Even amidst challenges, nature remains a source of healing, strength, and wonder."""

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

stop_words = set(stopwords.words('english'))
clean_words = []
for word in words:
    if word.isalpha() and word not in stop_words:
        clean_words.append(word)

ps = PorterStemmer()
stemmed = []
for w in clean_words:
    stemmed.append(ps.stem(w))

lm = WordNetLemmatizer()
lemmatized = []
for w in clean_words:
    lemmatized.append(lm.lemmatize(w))

print("Stemmed Words:", stemmed)
print("Lemmatized Words:", lemmatized)