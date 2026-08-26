#Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook
class Shirt:

    def __init__(self,sid=0,sname="unknown",type ="unknown",price = 0.0,size = "unknown"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt object {self.sid} is destroyed")   

    def ShowBook(self):
        print("Shirt ID:",self.sid)
        print("Shirt name:",self.sname) 
        print("Shirt type:",self.type)
        print("Shirt price:",self.price)
        print("Shirt Size:",self.size)

s1 = Shirt(201,"Over size","baggy",5654,"large")

s2 =Shirt()

print("-----SHIRT1------")
s1.ShowBook()
print("-----SHIRT2------")
s2.ShowBook()
