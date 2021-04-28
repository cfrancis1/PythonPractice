import random

i = 1

while i == 1:
    roll = input("Would you like to roll the dice? (type: 'yes' or 'no')\n")
    if(roll == "yes"):
        dice = random.randint(1,6)
        print(dice)
    else:
        print("Goodbye!")
        i = 0