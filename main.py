from src import api_call, vectorize_df, vectorize_input, comparison

def main():
    user_input = 'Norwegian Wood'
    title, genre, desc = api_call(user_input)
    df_vectors, mlb, desc_vect, title_vect, df = vectorize_df()
    user_vectors = vectorize_input(mlb, desc_vect, title_vect, title, genre, desc)
    
    recs = comparison(user_vectors, df_vectors)
    
    for idx in recs:
        print(df.iloc[idx]['title'])

if __name__ == "__main__":
    main()
