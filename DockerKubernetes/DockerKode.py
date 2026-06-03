import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("The computer will generate a number between 0 and 100, it will the try to guess it")
print("-------")
random_number = random.randint(0, 10)
guesses = 0
print("The number is:", random_number)
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