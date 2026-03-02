class Book:
    def __init__(self, title, price):
        print(f"Title: {title}")
        print(f"Price: {price}")

if __name__ == "__main__":
    b = Book("Python Core", 500)
