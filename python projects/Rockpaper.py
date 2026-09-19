import random

choices =["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").lower()
computer = random.choice(choices)
print(f"\nYou chose: {user}")
print(f"Computer chose:{computer}")

if user == computer:
    print("It is a Tie!")

elif user == "rock":
    if computer == "scissors":
        print("You Win!..")
    else:
        print("You lose!")  
elif user == "paper":
    if computer == "rock":
        print("You win!..")
    else:
        print("You loss...")     
elif user == "scissors":
    if computer == "paper":
        print("you win...")
    else:
        print("you loss....")

else:
    print("Invalid choice! plase chose rock, paper,scissors")                                 