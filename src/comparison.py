from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import load_npz

def comparison(user_input_vectors):
    df_vectors = load_npz('data/df_vectorized.npz')
    sims = cosine_similarity(user_input_vectors, df_vectors)
    top20 = sims[0].argsort()[::-1][:20]
    
    return top20
