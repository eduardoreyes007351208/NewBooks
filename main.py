from src import api_call, vectorize_input, comparison
from src.preprocessing import load_csv

def main():
    user_input = 'The Catcher in the Rye'
    title, genre, desc = api_call(user_input)
    user_vectors = vectorize_input(title, genre, desc)
    df = load_csv()
    recs = comparison(user_vectors)
    
    for idx in recs:
        print(f'{df.iloc[idx]['title']} by {df.iloc[idx]['author']}')

if __name__ == "__main__":
    main()
