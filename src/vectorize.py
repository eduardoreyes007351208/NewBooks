from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
from scipy.sparse import hstack

#rom sklearn.metrics.pairwise import cosine_similarity

def vectorize_input():
    pass

def vectorize_df():
    df = pd.read_csv('../data/clean_goodreads_100k_books.csv')
    mlb = MultiLabelBinarizer()
    desc_vectorizer = TfidfVectorizer(stop_words='english', max_features=50000)
    title_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_desc = desc_vectorizer.fit_transform(df['desc'])
    X_title = title_vectorizer.fit_transform(df['title'])
    X_genre = mlb.fit_transform(df['genre']).astype(float)
    
    X = hstack([2.0*X_desc, 1.0*X_title, 2.0*X_genre])
    
    print('Desc:', X_desc)
    print('Title: ',X_title)
    print('Genre: ', X_genre)
    print('Hstack: ', X)
    
    
vectorize_df()