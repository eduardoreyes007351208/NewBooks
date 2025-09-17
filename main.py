from src import api_call

def main():
    user_input = 'Norwegian Wood'
    title, genre, desc = api_call(user_input)
    print(title, genre, desc)


if __name__ == "__main__":
    main()
