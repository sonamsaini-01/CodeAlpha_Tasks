import random

def hangman():
    # List of possible words
    words = ["apple", "developer", "python", "school", "college", "hangman", "programming","sonam"]
    word = random.choice(words)  # Randomly choose a word
    guessed_word = ["_"] * len(word)  # Start with blanks
    guessed_letters = []  # Store guessed letters
    lives = 6  # Number of wrong attempts allowed

    print(" Welcome to Hangman!")
    print("Guess the word letter by letter.")
    print("You have", lives, "lives.\n")

    # Game loop
    while lives > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Lives left:", lives)

        guess = input("Enter a letter: ").lower()

        # Check input validity
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            lives -= 1
            print("❌ Wrong guess! You lost a life.\n")

    # End of game
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
hangman()
