#Create a class Complex Number with data members as real and imag and add
#following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Getter and setter
    def get_real(self):
        return self.real

    def set_real(self, real):
        self.real = real

    def get_imag(self):
        return self.imag

    def set_imag(self, imag):
         self.imag = imag
    
    

    # + operator
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    # - operator
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imag - other.imag
        )

    # Display
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Destructor
    def __del__(self):
        print("Object destroyed")


c1 = ComplexNumber(10, 20)
c2 = ComplexNumber(5, 10)

print("Real:", c1.get_real())
print("Imaginary:", c1.get_imag())

c1.set_real(15)
c1.set_imag(25)

print("After Setter:", c1)

c3 = c1 + c2
print("Addition:", c3)

c4 = c1 - c2
print("Subtraction:", c4)

