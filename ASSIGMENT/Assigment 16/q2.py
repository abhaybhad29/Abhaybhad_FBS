#Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.
class Product:
    discount = 10
    def __init__(self,pid="unkwons",pname="unkwons",price=0.0,quantity =0):
        self.pid= pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print("Constructor called")

    def apply_discount(self):
        discount_amount= self.price * Product.discount / 100
        self.price = self.price - discount_amount


    def showBook(self):
        print("product ID :",self.pid)
        print("product Name:",self.pname)
        print("price:",self.price)
        print("Quntity :",self.quantity)
        print("Discount :",Product.discount,"%")

    def __del__(self):
        print("Destructor called")

p1 = Product(101,"Laptop",50000,2)
p2= Product()
print("\nBefore Discount:")
p1.showBook()

p1.apply_discount()

print("\nAfter Discount")
p1.showBook()


p2 = Product()


print("\nDefault product")
p2.showBook()


