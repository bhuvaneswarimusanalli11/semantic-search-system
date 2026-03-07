from sklearn.datasets import fetch_20newsgroups
from utils.preprocessing import clean_text

def load_dataset():

    dataset = fetch_20newsgroups(subset='all')

    docs = dataset.data[:2000]   # limit dataset

    cleaned_docs = [clean_text(d) for d in docs]

    return cleaned_docs