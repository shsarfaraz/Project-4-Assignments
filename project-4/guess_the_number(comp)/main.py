import random
print("\nWelcome to Number Guessing Game!\n")

low = 1
high = 10

print("Think the Number Between 1-10 and computer will be guess the number!")

if low <= high:
    guess = random.randint(low, high)
    print ("Computer's Guess is: ", guess)

    while True:
        feedback = input("Is the guess is too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == 'C':
            print("Yah! The Computer Guessed Your Number ")
            break
        elif feedback == 'H':
            high = guess - 1
            guess = random.randint(low,high)
            print("Computer's Guess is: ", guess)
        elif feedback == 'L':
            low = guess + 1
            guess = random.randint(low,high)
            print("Computer's Guess is: ", guess)
        else:
            print("Invalid input. Please enter H, L or C")

if low > high:
    print("The Number is not in the range. Please try again. ")