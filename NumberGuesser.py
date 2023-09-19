from random import randint
import sys

random_num = randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Number Guesser! Our NumBot will choose a random number between 1 and 100. You will have 10 chances to correctly guess the number, so guess wisely!")
ready_or_not = input("Are you ready to begin the game? Y/N: ")

if ready_or_not == "Y":
    print(f"Hello this is NumBot. I have chosen a random number between 1 and 100. You will have {max_attempts} attempts to guess it.")
else:
    print("Ok see you next time!")
    sys.exit()

while attempts < max_attempts:
    try:
        usr_guess = int(input("Enter your guess: "))
        attempts += 1

        if usr_guess == random_num:
            print(f"Congrats! You guessed the number {random_num} in {attempts} attempts.")
            break
        elif usr_guess < random_num:
            print("The number you guessed is too low. Please try again.")
        else:
            print("The number you guessed it too high. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you have used up all {max_attempts} attempts. The random number was {random_num}.")