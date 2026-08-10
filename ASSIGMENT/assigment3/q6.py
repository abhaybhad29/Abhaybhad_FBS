#Write a program to calculate profit or loss.
CP = float(input("Enter the cost price :"))
SP = float(input("Enter the selling price :"))
if SP > CP :
    profit = SP - CP

    print("profit=",profit)
elif CP > SP :
    loss = CP - SP
    print("loss=",loss)
else:
    print("no profit,no loss")