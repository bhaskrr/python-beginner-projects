import random

def guess(num):
    random_number = random.randint(1, num*2)
    attempts = 0

    while True:
        user_guess = input(f"Guess the number (Between 1 and {num*2}) or 'q' to quit: ")
        
        if user_guess.lower() == 'q':
            print("Thanks for playing!")
            break
        
        if not user_guess.isdigit():
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        if user_guess < 1 or user_guess > num*2:
            print("Please enter a number within the specified range.")
            continue
        
        if user_guess < random_number:
            print("Too low!")
        elif user_guess > random_number:
            print("Too high!")
        else:
            print(f"Yay! You have guessed the number {random_number} in {attempts} attempts.")
            break

guess(random.randint(10, 20))