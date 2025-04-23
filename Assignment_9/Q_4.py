import re

# Original paragraph from Q1
text = """Technology has revolutionized the way we live, work, and connect with others. 
From smartphones to artificial intelligence, it continues to shape our daily experiences. 
The internet has made knowledge more accessible than ever before. 
Innovations in robotics and automation are changing industries rapidly. 
While there are concerns about privacy and over-dependence, technology also opens doors to endless possibilities and progress.
Contact us at support@example.com or visit https://techworld.com.
For inquiries, call +91 9876543210 or 123-456-7890."""

def custom_tokenizer(text):
    clean_text = re.sub(r"[^a-zA-Z0-9\-'.\s]", ' ', text)
    pattern = r"\b(?:\d+\.\d+|\d+|[a-zA-Z]+(?:-[a-zA-Z]+)*|'[a-z]+)\b"
    tokens = re.findall(pattern, clean_text)

    return tokens


def clean_text_regex(text):
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '<EMAIL>', text)
    text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text)
    text = re.sub(r'(\+?\d{1,3}[\s\-]?)?\d{3}[\s\-]?\d{3}[\s\-]?\d{4}', '<PHONE>', text)

    return text


cleaned_text = clean_text_regex(text)
tokens = custom_tokenizer(cleaned_text)

print("Cleaned Text:\n", cleaned_text)
print("\nCustom Tokens:\n", tokens)
