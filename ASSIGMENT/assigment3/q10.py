#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)
G = input("Enter the gender (m/f) :")
age = int(input("Enter the age :"))
if (G == 'f'):
    if(age >=18):
        print("eligible.")
    else:
        print("not eligible.")
        
else:
    
        if(age >=21):
            print("eligible.")
        else:
            ("not eligible.")
