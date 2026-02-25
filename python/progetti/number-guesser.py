import random

print("Welcome to the Number Guesser Game!\nTry to guess the number between 1 and 10.")
random_number = random.randrange(1, 10)
while True:
    user_number = input("Enter a number: ")
    if user_number == str(random_number):
        print("\nYou guessed it! The number was " + str(random_number) + "\nSee you next time!")
        break
    else:
        print("\nOh no! Wrong number...")
    
    new_try = input("\nWant to try again?\nEnter Y for yes or N for no: ")

    if new_try == "n" or new_try == "N":
        print("\nOk, just to let you know the number was " + str(random_number) + ".\nSee you next time!")
        break
    elif new_try == "y" or new_try == "Y":
        print("\nPerfect, let's try again.")
        continue
    else:
        print("\nInvalid answer. Restarting the game...")
        continue