from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
from scipy.sparse import hstack, save_npz, load_npz
import pickle


def vectorize_input(mlb, desc_vec, title_vec, title, genre, desc):
    
    X_desc = desc_vec.transform([desc])
    X_title = title_vec.transform([title])
    X_genre = mlb.transform([genre]).astype(float)
    
    new_X = hstack([3.0*X_desc, 0.5*X_title, 1.0*X_genre])
    
    return new_X

def vectorize_df():
    df = pd.read_csv('data/clean_goodreads_100k_books.csv')
    mlb = MultiLabelBinarizer()
    desc_vectorizer = TfidfVectorizer(stop_words='english', max_features=50000)
    title_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_desc = desc_vectorizer.fit_transform(df['desc'])
    X_title = title_vectorizer.fit_transform(df['title'])
    X_genre = mlb.fit_transform(df['genre']).astype(float)
    
    X = hstack([3.0*X_desc, 0.5*X_title, 1.0*X_genre])
    
    return X, mlb, desc_vectorizer, title_vectorizer, df
    
    
    
    
vectorize_df()
#vectorize_input()