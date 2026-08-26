#Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook
class Product:
    def __init__(self,pid=0,pname="Unknowons",price=0.0,quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"product object {self.paid} is destroyed")

    def Showproduct(self):
        print("Product id:",self.pid)
        print("product name :",self.pname) 
        print("product price:",self.price)
        print("product quantity:",self.quantity)

p1 = Product(101,"laptop",44675,2)

p2 = Product()

print("-----product1------")
p1.Showproduct()
print("-----product2------")
p2.Showproduct()