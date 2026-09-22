#Create a class Distance with data members as km,m and cm and add following
#methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator


class Distance:

    # Constructor
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    # Getter and setter
    
    def get_km(self):
        return self.km
    def set_km(self, km):
            self.km = km

    def get_m(self):
        return self.m
    def set_m(self, m):
            self.m = m

    def get_cm(self):
        return self.cm
    def set_cm(self, cm):
            self.cm = cm

    
    # + operator
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # - operator
    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 - total2

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    # Display
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    # Destructor
    def __del__(self):
        print("Object destroyed")


# Create objects
d1 = Distance(5, 600, 80)
d2 = Distance(2, 500, 50)

# Getter
print("Kilometer:", d1.get_km())
print("Meter:", d1.get_m())
print("Centimeter:", d1.get_cm())

# Setter
d1.set_km(6)
d1.set_m(700)
d1.set_cm(90)

print("After Setter:", d1)

# Addition
d3 = d1 + d2
print("Addition:", d3)

# Subtraction
d4 = d1 - d2
print("Subtraction:", d4)