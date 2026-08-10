#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
correct_id = "Abhay23"
Correct_pass = "234032"
attempt = 1
while attempt <= 3:
    id = input("Enter a userid :")
    password = input("Enter the password :")
    if id == correct_id and password == Correct_pass:
        print("Login succefully.")
        break
    else:
        print("ID or password invaide.")
        if attempt < 3 :
            print("Attempt left ", 3 - attempt)
    attempt +=1
    if attempt > 3:
        print("pragram terminate.")        