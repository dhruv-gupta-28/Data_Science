class Book:
    def set_details(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: {self.title} by {self.author}")

if __name__ == "__main__":
    b = Book()
    b.set_details("1984", "George Orwell")
    b.display()
