#Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.
class Book:
    count = 0
    def __init__(self,bid=0,bname ="Unkwons",price =0.0,author ="Unkwons"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count +=1

    def __del__(self):
        print(f"Book object{self.bid} is destroyed")

    def ShowBook(self):
        print("Book ID :",self.bid)
        print("Book name:",self.bname)
        print("Book price:",self.price)
        print("Book author:",self.author)

b1 = Book(101, "love life", 500, "sakshi")
b2 = Book(102, "love zone", 600, "sarthak")
b3 = Book()       

print("----BOOK1----")
b1.ShowBook()
print("\n----BOOK2----")
b2.ShowBook()
print("\n----BOOK3----")
b3.ShowBook()

print("\nTotal Objects Created :", Book.count)
