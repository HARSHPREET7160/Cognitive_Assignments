import re

# Original paragraph (from Q1)
text = """Technology has revolutionized the way we live, work, and connect with others. 
From smartphones to artificial intelligence, it continues to shape our daily experiences. 
The internet has made knowledge more accessible than ever before. 
Innovations in robotics and automation are changing industries rapidly. 
While there are concerns about privacy and over-dependence, technology also opens doors to endless possibilities and progress."""

words_gt5 = re.findall(r'\b[a-zA-Z]{6,}\b', text)

numbers = re.findall(r'\b\d+\b', text)

capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)

alpha_only_words = re.findall(r'\b[a-zA-Z]+\b', text)

vowel_words = [word for word in alpha_only_words if re.match(r'^[aeiouAEIOU]', word)]

print("Words with more than 5 letters:\n", words_gt5)
print("\nNumbers in the text:\n", numbers if numbers else "No numbers found.")
print("\nCapitalized Words:\n", capitalized_words)
print("\nAlphabet-only words:\n", alpha_only_words)
print("\nWords starting with a vowel:\n", vowel_words)
