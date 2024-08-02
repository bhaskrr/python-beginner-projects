import random

def get_user_input():
    while True:
        try:
            number = int(input("Enter the number to guess: "))
            if number <= 0:
                print("Please enter a positive integer.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def computer_guess(number):
    low = 1
    high = number
    guesses = 0
    while True:
        guesses += 1
        guess = random.randint(low, high)
        print(f"Computer's guess is: {guess}")
        if guess == number:
            print(f"The computer has guessed the number {number} correctly in {guesses} guesses!")
            break
        elif guess < number:
            print("Too low!")
            low = guess + 1
        else:
            print("Too high!")
            high = guess - 1

number = get_user_input()
computer_guess(number)