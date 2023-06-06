class Library:
    def __init__(self):
        self.book = [
            "The Great Gatsby",
            "1984",
            "To Kill a Mockingbird",
            "The Catcher in the Rye",
            "Pride and Prejudice",
            "Crime and Punishment",
            "One Hundred Years of Solitude",
            "Beloved",
            "The Lord of the Rings"
        ]
        print(f'Length of list is {len(self.book)}')
    
    def books(self):
        return self.book
    
    def append(self, book):
        self.book.append(book)

a = Library()
print(a.books())
a.append('Go to hell')
print(a.books())
