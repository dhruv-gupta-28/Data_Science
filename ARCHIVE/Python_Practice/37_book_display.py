class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

if __name__ == "__main__":
    b = Book("The Alchemist", "Paulo Coelho")
    b.display()
