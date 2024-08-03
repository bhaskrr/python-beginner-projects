import random, string

def choose_word():
    words = [
        "python", "hangman", "programming", "developer", "software", 
        "algorithm", "function", "variable", "loop", "condition"
    ]
    return random.choice(words)

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    
    # while loop
    while len(word_letters) > 0:
        guessed_word = [letter if letter in used_letters else '_' for letter in word]
        print("The word is: ", " ".join(guessed_word))
        print(f"You have used letters: ", " ".join(used_letters))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print(f"You have guessed the letter {user_letter} right!")
                word_letters.remove(user_letter)
            elif user_letter not in word_letters:
                print(f"The letter {user_letter} is not in the word!")
        elif user_letter in used_letters:
            print(f"You have already guessed the letter {user_letter}!")
        else:
            print("Please enter a valid letter!")
        
    print(f"Yay! You have guessed the word {word} correctly!")
hangman()