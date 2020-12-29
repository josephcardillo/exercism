def two_fer(name="you"):
    return f"One for {name}, one for me."

# def fav_book(book="I don't like to read."):
#     if book != "I don't like to read.":
#         print(f"My favorite book is {book}.")
#     else:
#         print(book)

def fav_book(*books):
    if books:
        for book in books:
            print(f"My favorite book is {book}.")
    else:
        print("I don't like to read.")

# def fav_book(book):
#     try:
#         print(f"My favorite book is {book}.")
#     except:
#         print("I don't like to read.")
#     finally:
#         print("I don't like to read.")