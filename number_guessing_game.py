import random

def guessing_game():
    number = random.randint(1, 100)
    
    tries = 0

    while True:
        if tries > 2:
            print("Sorry, you had too many tries!")
            break
        guess_number = int(input("Enter any number between 1 and 100... "))
        if int(guess_number) == number:
            print(f"Your choice of {guess_number} is just right!")
            break
        if guess_number < number:
            print(f"Your choice of {guess_number} is less than the secret number")
            tries += 1
        else:
            print(f"Your choice of {guess_number} is more than the secret number")
            tries += 1

guessing_game()