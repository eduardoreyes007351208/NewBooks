import pandas as pd

def load_csv():
    df = pd.read_csv('data/clean_goodreads_100k_books.csv')
    return df