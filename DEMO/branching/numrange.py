num = int(input("Enter the number :"))
if num>=1:
    if num <= 250 :
        if num <= 50 :
            print("The range is : 1-50.")
        else:
            if num <= 100 :
                print("The range is : 51-100.")
            else:
                if num <= 150 :
                    print("The range is : 101 - 150.")
                else:
                    if num <= 200 :
                        print("The range is :151- 200.")
                    else:
                        print("The range is :201-250.")
                        
                            #print("The range is :201-250.")
    else:
        print("The num is greter than 250.")
else:
    print("The num is less than 1.")        