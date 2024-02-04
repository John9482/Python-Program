import random

# Generate a random number between 1 and 100
lucky_number = random.randint(1, 100)

# Ask the user to enter a number
guess = int(input("Enter a number between 1 and 100: "))

# Check if the guessed number is the lucky number
if guess == lucky_number:
    print("Congratulations! You've won the game.")
else:
    print("Sorry, try again next time.")
