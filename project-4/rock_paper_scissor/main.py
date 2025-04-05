import random
print("\nWelcome to the Rock, Paper, Scissors Game!\n")

choices = ["rock", "paper", "scissors"]
user_score = computer_score = 0
print("Lets Play!\n")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print(f"Final Score - You: {user_score} Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")

    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

print(f"\nYour score: {user_score}")
print(f"\nComputer score: {computer_score}")

