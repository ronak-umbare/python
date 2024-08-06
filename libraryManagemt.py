class Library:
    def __init__(self):
        self.no_books = 0
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        self.no_books = len(self.books)
    
    def show_info(self):
        print(f"The library has {self.no_books} books \n")
        
       
l1 = Library()
no = int(input("Enter the no. of biooks u wanna read"))
for i in range(no):
     bks = input("Enter books = ")
     l1.add_book(bks)
l1.show_info()

