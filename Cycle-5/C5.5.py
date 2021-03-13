#5. Create a class Publisher (name). Derive class Book from Publisher with attributes title  and author. Derive class Python from Book with attributes price and no_of_pages. Write a program that displays information about a Python book. Use base class constructor invocation and method overriding.
class Publisher:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("The publisher of the book is Morris V.")

class Book(Publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("The title of the book is ", self.title)
        print("The author of the book is ", self.author)

class Python(Book):
    def __init__(self,price, pages):
        self.price=price
        self.pages=pages
    def display(self):
        print("The price of the book is ", self.price)
        print("Total pages of the book is ", self.pages)

obj=Python(15000,3000)
obj.show()
obj.display()