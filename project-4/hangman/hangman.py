import random
import string
from words import words  # Import the list of words from the words.py file

def get_valid_word(words):
    word = random.choice(words).upper()  # Convert the word to uppercase
    while '-' in word or ' ' in word:  # Make sure no word contains a hyphen or space
        word = random.choice(words).upper()  # Re-pick and convert to uppercase
    return word

def hangman():
    word = get_valid_word(words)  # Random word chosen from the list (in uppercase now)
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of all uppercase letters
    used_letters = set()  # Set of all guessed letters (correct or incorrect)
    incorrect_guesses = 0  # Counter for incorrect guesses

    print("Welcome to Hangman!")
    
    while len(word_letters) > 0:  # Loop until all letters are guessed
        print(f"You have used these letters: {' '.join(sorted(used_letters))}")
        
        # Word display with guessed letters or "-" for unguessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        # Get user input
        user_letter = input('Guess a letter: ').upper()  # Convert to uppercase for uniform comparison

        # Debugging: Show what the user input is
        print(f"User guessed: {user_letter}")

        # Check if the input is a valid letter and hasn't been guessed before
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)  # Add guessed letter to used_letters

            # If the guessed letter is in the word, remove it from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove letter from word_letters
            else:
                print(f"{user_letter} is not in the word.")
                incorrect_guesses += 1  # Increase incorrect guess counter
        elif user_letter in used_letters:  # If letter was guessed already
            print("You have already used that character. Please try again.")
        else:  # If the character is invalid
            print("Invalid character. Please try again.")

        # End the game if too many incorrect guesses
        if incorrect_guesses >= 6:
            print("Sorry, you've lost the game!")
            print(f"The correct word was: {word}")
            break

    else:  # If the word is fully guessed
        print(f"Congratulations! You've guessed the word: {word}")

# Run the game
hangman()
