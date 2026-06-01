import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("--------------------------------")
print("I will pick a random number between 0 and a number you choose, and you have to guess it!")
user_input = input("Type a number:")
print("--------------------------------")

clear_screen()

if user_input.isdigit():
    user_input = int(user_input)

    if user_input <= 0:
        print("It has to be a number larger than 0!")
        print("Exiting program...")
        time.sleep(2)
        quit()
else:
    print("Type a number next time!")
    print("Exiting program...")
    time.sleep(2)
    quit()

random_number = random.randint(0, user_input)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Try and guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number!")
        continue

    if user_guess == random_number:
        print("Congratulations! You guessed the number!")
        break
    elif user_guess > random_number:
        print("You guessed above the number, try again")
        continue
    else:
        print("You guessed below the number, try again")
        continue

print("It took you", guesses, "tries to guess the number.")