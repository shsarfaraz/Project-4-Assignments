import random

print("\nWelcome to the Number Guessing Game!\n")

secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue  
        
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
