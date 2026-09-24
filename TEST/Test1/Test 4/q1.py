#Write a function to which we pass a parameter and
#print the factors of a given number
#For Eg: Factors of 12 : 1,2,3,4,6,12
def factorial(n):
    print("Factors of",n, ":",end = " ")
    for i in range(1,n+1):
        if n % i ==0:
            print(i,end =" ")
factorial(16)   

