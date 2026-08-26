#1. Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
class Book:
    def __init__(self,bid=0,bname="Unknown",price=356, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author


# Destructor
    def __del__(self):
        print(f"Book object {self.bid} is destroyed")

# ShowBook method
    def ShowBook(self):
        print("Book ID   :",self.bid)
        print("Book Name :",self.bname)
        print("price     :",self.price)
        print("author    :",self.author)


# Parameterized constructor

b1 =Book(101,"love failure",556,"Rutvik")

# Parameterless constructor
b2 =Book()
print("----- Book 1 -----")
b1.ShowBook()

print("\n----- Book 2 -----")
b2.ShowBook()


     
