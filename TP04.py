class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

class Ebook(Book):
    def __init__(self, title, auther, price, file_size):
        super().__init__(title, auther, price)
        self.file_size = file_size

book1 = Book("Python Basics", "John Smith", 20)

print("Book Information")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.get_price())

book1.set_price(25)
print("New price:", book1.get_price())

print("---------------------")

ebook1 = Ebook("Python Advanced", "David", 30, "5 MB")

print("Ebook Information")
print("title:", ebook1.title)
print("Author:", ebook1.author)
print("Price:", ebook1.get_price())
print("File Size:", ebook1.file_size)