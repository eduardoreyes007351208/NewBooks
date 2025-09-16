import requests

url = 'https://www.googleapis.com/books/v1/volumes'
def api_call(title):
    q = title.lower()
    params = {
        'q': q,
        'maxResults': 10,
        'printType': 'books'
    }
    
    response = requests.get(url, params=params).json()
    book_data = response['items'][0]['volumeInfo']
    title = book_data.get('title')
    author = book_data.get('authors')
    category = book_data.get('categories')
    print(title, author, category)
    
    
api_call('The Song of Achilles')