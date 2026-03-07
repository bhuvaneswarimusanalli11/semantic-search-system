import re

def clean_text(text):

    text = text.lower()

    text = re.sub(r'\S+@\S+', '', text)

    text = re.sub(r'[^a-zA-Z ]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text