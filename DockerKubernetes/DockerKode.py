import random
import os
import time

# def clear_screen():
    # .system('cls' if os.name == 'nt' else 'clear')

# clear_screen()

def PrintNumber():
    print("the number is:", random_number)

"""
Program that generates a random number and then tries to guess it.
it will keep track of how many guesses it takes to guess the number. 
The program will also give feedback on whether the guess is too high or too low.
"""

print("The computer will generate a number between 0 and 10, it will the try to guess it")
print("-------")
random_number = random.randint(0, 10)
guesses = 0
PrintNumber()
print("-------")

time.sleep(2)
print("I will now guess the number")

while True:
    guesses += 1
    time.sleep(1)
    user_guess = random.randint(0,10)
    print("My guess is:", user_guess)
    
    if user_guess == random_number:
        print("Horray! I guessed the number!")
        break
    elif user_guess > random_number:
        print("I guessed too high this time")
        continue
    else:
        print("I guessed too low this time")
        continue

print("It only took me", guesses, "tries to guess the number.")