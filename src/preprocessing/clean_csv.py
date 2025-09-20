# import pandas library
import pandas as pd

# define clean_csv module/function
def clean_csv():
    # initialize dataframe that contains data from dataset
    df = pd.read_csv('../../data/GoodReads_100k_books.csv')
    # new dataframe that drops empty cells
    new_df = df.dropna()
    # new dataframe that drops columns that aren't needed
    new_df_1 = new_df.drop(columns=['bookformat', 'img', 'isbn', 'isbn13', 'link', 'pages', 'rating', 'reviews', 'totalratings'])
    # saves clean dataframe as csv with clean data for vectorization
    new_df_1.to_csv(r'../../data/clean_goodreads_100k_books.csv', index=False)

# calling clean_csv function
if __name__ == "__main__":
    clean_csv()
