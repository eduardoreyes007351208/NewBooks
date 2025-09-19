from sklearn.metrics.pairwise import cosine_similarity

def comparison(user_input_vectors, df_vectors):
     
    sims = cosine_similarity(user_input_vectors, df_vectors)
    top20 = sims[0].argsort()[::-1][:10]
    
    return top20
