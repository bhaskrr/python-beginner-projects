import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
QUIT = 'q'

def play():
    while True:
        user_choice = input(f"What's your choice? '{ROCK}' for rock, '{PAPER}' for paper, '{SCISSORS}' for scissors or '{QUIT}' to quit: ")
        user_choice = user_choice.lower()
        if user_choice == QUIT:
            print('Thanks for playing!')
            break
        elif user_choice not in [ROCK, PAPER, SCISSORS]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = random.choice([ROCK, PAPER, SCISSORS])

        print(f"Player: {user_choice}")
        print(f"Computer: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie")
        elif is_player_winner(user_choice, computer_choice):
            print('You won!')
        else:
            print('You lost!')

def is_player_winner(player, computer):
    """Determine if the player wins based on their choice and the computer's choice"""
    if (player == ROCK and computer == SCISSORS) or (player == PAPER and computer == ROCK) or (player == SCISSORS and computer == PAPER):
        return True
    return False

# Play the game
play()