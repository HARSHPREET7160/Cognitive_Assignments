from textblob import TextBlob
from wordcloud import WordCloud

feedback = "The keyboard feels cheap and the keys are unresponsive."

analysis = TextBlob(feedback)
polarity = analysis.sentiment.polarity
subjectivity = analysis.sentiment.subjectivity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Polarity:", polarity)
print("Subjectivity:", subjectivity)
print("Sentiment:", sentiment)

if sentiment == "Positive":
    wordcloud = WordCloud().generate(feedback)
    wordcloud.to_file("positive_feedback.png")
