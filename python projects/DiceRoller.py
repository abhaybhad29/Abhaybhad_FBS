import random

def roll_dice():
    """Roll a dice and returns a random number between 1 to 6."""
    return random.randint(1,6)

#Main program
print("Welcome to Dice Roller!")


while True:
    input_choice = input("Press Enter to roll the dice(or 'q' to quit): ")
    if input_choice.lower() == 'q' :
        print("Thanks for playing! Goodbye.")
        break
    result = roll_dice()
    print(f"You rolled: {result}")