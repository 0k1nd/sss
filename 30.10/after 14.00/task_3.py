class Author():
    
    def __init__(self, name, books = []):
        self.name = name
        self.books = books
        
    def display_books(self):
        for i, element in enumerate(self.books):
            print((i + 1), element)
        
    def add_book(self, book):
        self.books.append(book)
        
    def get_books_by_year(self, year):
        finded_book =[]
        for book in self.books:
            if book.year == year:
                finded_book.append(book.title)
        return finded_book
        
class Book():
    
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def __repr__(self):
        return f'(\'{self.title}\', {self.year})'
    
ew = Author('Paulo Coelho') 
rer = Book('s545as', 1944)
pou = Book('jynhgs', 1)
rfv = Book('sdas', 1944)
qaz = Book('s4s', 4)
wsx = Book('sxcvs', 1488)
by = Book('swe', 1933)

ew.add_book(rer)
ew.add_book(pou)
ew.add_book(rfv)
ew.add_book(wsx)
ew.add_book(by)
ew.display_books()
ew.get_books_by_year(1944)
print(ew.get_books_by_year(1944))

        
        