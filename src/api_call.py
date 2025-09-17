# import requests library to get book data from api
import requests

# initialize the url for the Google Book API
url = 'https://www.googleapis.com/books/v1/volumes'

# initialize the module api_call which calls to api and returns book info
def api_call(title):
    # book title query from user
    q = title.lower()
    # parameters that will be used in the api call
    params = {
        'q': q,
        'maxResults': 10,
        'printType': 'books'
    }
    
    # api call using url and parameters, returned as json
    response = requests.get(url, params=params).json()
    # setting book_data to the information from the first book returned by api
    book_data = response['items'][0]['volumeInfo']
    # setting the book title, genres of the book, and the book description
    book_title = book_data['title']
    genres = book_data['categories']
    desc = book_data['description']
    
    # returning the book info
    return book_title, genres, desc
    
