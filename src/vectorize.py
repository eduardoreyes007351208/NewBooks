from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
from scipy.sparse import hstack, save_npz
import pickle


def vectorize_input(title, genre, desc):
    
    with open('data/desc_vectorizer.pkl', 'rb') as f:
        desc_vec = pickle.load(f)
    with open('data/title_vectorizer.pkl', 'rb') as f:
        title_vec = pickle.load(f)
    with open('data/mlb_genre.pkl', 'rb') as f:
        mlb = pickle.load(f)
    
    X_desc = desc_vec.transform([desc])
    X_title = title_vec.transform([title])
    X_genre = mlb.transform([genre]).astype(float)
    
    new_X = hstack([2.0*X_desc, 1.0*X_title, 2.0*X_genre])
    
    return new_X

def vectorize_df():
    df = pd.read_csv('../data/clean_goodreads_100k_books.csv')
    mlb = MultiLabelBinarizer()
    desc_vectorizer = TfidfVectorizer(stop_words='english', max_features=15000,  ngram_range=(1,2))
    title_vectorizer = TfidfVectorizer(stop_words='english', max_features=2000,  ngram_range=(1,2))
    X_desc = desc_vectorizer.fit_transform(df['desc'])
    X_title = title_vectorizer.fit_transform(df['title'])
    X_genre = mlb.fit_transform(df['genre']).astype(float)
    
    X = hstack([3.0*X_desc, 0.5*X_title, 1.0*X_genre])
    
    save_npz('../data/df_vectorized.npz', X)
    with open('../data/desc_vectorizer.pkl', 'wb') as f:
        pickle.dump(desc_vectorizer, f)
    with open('../data/title_vectorizer.pkl', 'wb') as f:
        pickle.dump(title_vectorizer, f)
    with open('../data/mlb_genre.pkl', 'wb') as f:
        pickle.dump(mlb, f)
    

if __name__ == "__main__":
    vectorize_df()
    

#vectorize_input()