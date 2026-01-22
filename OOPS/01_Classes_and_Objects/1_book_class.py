"""
1. Create a class `Book` with:
   - instance variables `title` and `author`
   - method `display()` to print book details
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")

if __name__ == "__main__":
    b1 = Book("The Alchemist", "Paulo Coelho")
    b1.display()
