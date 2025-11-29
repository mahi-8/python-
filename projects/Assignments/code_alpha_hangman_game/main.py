import random

def display_hangman(lives):
    """Returns the ASCII art for the hangman based on remaining lives."""
    stages = [
        # Stage 0 (6 incorrect guesses)
        r"""
           -----
           |   |
           O   |
          /|\  |
          / \  |
               -
        """,
        # Stage 1
       r"""
           -----
           |   |
           O   |
          /|\  |
          /    |
               -
        """,
        # Stage 2
       r"""
           -----
           |   |
           O   |
          /|\  |
               |
               -
        """,
        # Stage 3
       r"""
           -----
           |   |
           O   |
          /|   |
               |
               -
        """,
        # Stage 4
       r"""
           -----
           |   |
           O   |
           |   |
               |
               -
        """,
        # Stage 5
        r"""
           -----
           |   |
           O   |
               |
               |
               -
        """,
        # Stage 6 (0 incorrect guesses, game starts here)
       r"""
           -----
           |   |
               |
               |
               |
               -
        """
    ]
    # We use (6 - lives) because 6 lives means index 0 (full figure)
    # The list is defined backwards, so we index it correctly:
    return stages[6 - lives]


def hangman_game():
    # --- 1. PREPARATION ---
    word_list = ["PYTHON", "HANGMAN", "CODING", "PROGRAM", "VARIABLE", "FUNCTION"]
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    
    # --- 2. SETUP ---
    lives = 6
    guessed_letters = []
    # Create a list for the display: ['_', '_', '_', ...]
    display = ["_"] * word_length 
    game_over = False

    print("--- ⚔️ Welcome to Hangman! ⚔️ ---")

    # --- 3. GAME LOOP ---
    while not game_over:
        print(display_hangman(lives))
        print(f"\n{ ' '.join(display) }")
        print(f"Guessed letters: { ', '.join(sorted(guessed_letters)) }")
        print(f"Lives remaining: {lives}\n")

        # --- 4. GUESS & CHECK ---
        guess = input("Guess a letter: ").upper()

        # Input Validation (Check 1: Already guessed?)
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Input Validation (Check 2: Valid input?)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        # Record the guess
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            # CORRECT GUESS: Update the display list
            for i in range(word_length):
                if secret_word[i] == guess:
                    display[i] = guess
            print("Correct! 🎉")
        else:
            # INCORRECT GUESS: Reduce lives
            lives -= 1
            print("Incorrect guess! 😔")

        # --- 5. END GAME CHECK ---
        if "_" not in display:
            game_over = True
            print(display_hangman(lives))
            print(f"\nWINNER! The word was {secret_word}.")
        
        elif lives == 0:
            game_over = True
            print(display_hangman(lives))
            print(f"\nGAME OVER! The word was {secret_word}.")

# Start the game
hangman_game()