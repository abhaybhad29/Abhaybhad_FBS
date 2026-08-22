#Python Program to Generate a Dictionary that Contains Numbers (between 1
#and n) in the Form (x,x*x).
def generate_dictionary(n):
    d = {}
    for x in range(1,n+1):
        d[x] = x * x

    return d

n = int(input("Enter the value of n :"))

result = generate_dictionary(n)
print("Dictionary :",result)