"""Oops Machine test

Create a base class called Book with the following attributes and methods:
Attributes:
title (string): The title of the book.
author (string): The author of the book.
price (float): The price of the book.
Methods:
_init_(self, title, author, price): Constructor method to initialize the attributes.
get_details(self): Method that returns a string containing the title, author, and price of the book.
Create three subclasses Fiction, NonFiction, and Poetry, each inheriting from the Book class. Each subclass
should have an additional attribute:

For Fiction: genre (string): The genre of the fiction book (e.g., Mystery, Romance, Science Fiction, etc.).
For NonFiction: topic (string): The topic of the non-fiction book (e.g., History, Science, Self-Help, etc.).
For Poetry: style (string): The style of the poetry (e.g., Sonnet, Haiku, Free Verse, etc.).
Each subclass should also override the get_details() method to include its specific attribute.

Create a class called Bookstore with the following attributes and methods:
Attributes:

name (string): The name of the bookstore.
books (list of Book objects): A list to store all the book objects.
Methods:
_init_(self, name): Constructor method to initialize the name of the bookstore.
add_book(self, book): Method that takes a Book object as input and adds it to the list of books.
display_books(self): Method that displays the details of all the books in the bookstore.

Your task is to implement the above scenario by creating the required classes and methods. Also,
create instances of each book type and add them to the bookstore. Finally, display the details of all
the books in the bookstore.

"""


#
# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def get_details(self):
#         print("book title:",self.title)
#         print("author:",self.author)
#         print("price:",self.price)
# class fiction(book):
#     def  __init__(self,title,author,price,genre):
#         super().__init__(title,author,price)
#         self.genre=genre
#
#     def get_details(self):
#       fdetail=super().get_details()
#       print(fdetail,"genre:",self.genre)
#
# class nonfiction(book):
#     def  __init__(self,title,author,price,topic):
#         super().__init__(title,author,price)
#         self.topic=topic
#
#     def get_details(self):
#         ndetail = super().get_details()
#         print(ndetail, "topic:", self.topic)
#
#
#
#
# class poetry(book):
#     def  __init__(self,title,author,price,style):
#         super().__init__(title,author,price)
#         self.style=style
#
#     def get_details(self):
#         pdetail = super().get_details()
#         print(pdetail, "style:", self.style)
# obj3=book("alchi","john",2005)
# obj3.get_details()
# obj=fiction("ree","amm",99,"mystery")
# obj.get_details()
# obj1=nonfiction("ree","amm",99,"histry")
# obj1.get_details()
# obj2=poetry("ree","amm",99,"sonnet")
# obj2.get_details()


class bookstore:
    def __init__(self,name):
        self.name = name


    def add_book(self,book):
        self.book=book


    def display_book(self):
          print("bookstore:",self.book)
obj=bookstore("amm")

obj.display_book()












