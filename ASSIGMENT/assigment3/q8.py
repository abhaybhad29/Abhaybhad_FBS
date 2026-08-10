#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)
import random
userId = input("Enter the user id :")
password = input("Enter the password :")
if userId =="admin" and password == "rohit@123":
    captch = random.randint(1000,9999)
    #captch = random.randint(1000, 9999)

    print("captch =",captch)

    user_captcha = int(input("Enter the captcha :"))

    if user_captcha == captch :
        print("login succefully. ")

    else:
        print("captcha verification failed")

else:
    print("Invaid user id or pass.")