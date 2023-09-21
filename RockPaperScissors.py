import random

# Define the game's rules
choices = ["Rock", "Paper", "Scissors"]
beats = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

while True:
    # Get user input
    user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    if user_choice in choices:
        # Generate computer's choice
        computer_choice = random.choice(choices)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif beats[user_choice] == computer_choice:
            result = "You win!"
        else:
            result = "Computer wins!"

        # Display the result
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
