#Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
#xlarge=1300) Use static concept.
class Shirt:
    size_price ={
        "small":0,
        "medium":10,
        "large":20,
        "xlarge":30
    }

    def __init__(self,sid=0,sname="unknown",type="Formal",price="0.0",size="small"):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        print("Constructor called")

    @staticmethod
    def calculate_price(price,size):
        if size.lower() =="small":
            return size
        elif size.lower() =="medium":
            return price +(price*10/100)
        elif size.lower() == "large":
            return price + (price* 20 / 100)
        elif size.lower() =="xlarge":
            return price + (price * 30/ 100)
        else:
            return price

    def showBook(self):
        final_price = Shirt.calculate_price(self.price, self.size)

        print("Shirt ID    :", self.sid)
        print("Shirt Name  :", self.sname)
        print("Type        :", self.type)
        print("Size        :", self.size)
        print("Price       :", final_price)

    
    def __del__(self):
        print("Destructor called")



s1 = Shirt(101, "Arrow Shirt", "Formal", 1000, "small")
s1.showBook()

print()

s2 = Shirt(102, "Peter England", "Formal", 1000, "medium")
s2.showBook()

print()

s3 = Shirt(103, "Louis Philippe", "Formal", 1000, "large")
s3.showBook()

print()
s4 = Shirt(104, "Van Heusen", "Formal", 1000, "xlarge")
s4.showBook()

print()


s5 = Shirt()
s5.showBook()
    


