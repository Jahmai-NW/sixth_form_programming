class Book():

    # Constructor
    def __init__ (self, theTitle, theAuthor, theYear):
        self.title = theTitle
        self.author = theAuthor
        self.year = theYear

    # Getters
    def getBookInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")

# Child Classes
class Fiction(Book):

    # Construtor + inherit parent
    def __init__ (self, theTitle, theAuthor, theYear, theGenre):
        super().__init__(theTitle, theAuthor, theYear)
        self.genre = theGenre

    # Getters
    def getBookInfo(self):
        super().getBookInfo()
        print(f"Genre: {self.genre}")

class NonFiction(Book):

    # Construtor + inherit parent
    def __init__ (self, theTitle, theAuthor, theYear, theSubject):
        super().__init__(theTitle, theAuthor, theYear)
        self.subject = theSubject

    def getBookInfo(self):
        super().getBookInfo()
        print(f"Subject: {self.subject}")


######################

# Create Fiction and NonFiction books
fiction_book = Fiction("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Drama")
nonfiction_book = NonFiction("Sapiens", "Yuval Noah Harari", 2011, "History")

# Display their details
print("Fiction Book Details:")
fiction_book.getBookInfo()

print("\nNon-Fiction Book Details:")
nonfiction_book.getBookInfo()