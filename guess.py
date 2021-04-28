import random

i = 1
answer = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100.\n"))

while i == 1:
    if(guess < answer):
        guess = int(input("The answer is a larger number, guess again\n"))
    elif(guess > answer):
        guess = int(input("The answer is a smaller number, guess again\n"))
    elif(guess == answer):
        print("You got it! The answer was " + str(answer))
        i = 0