import random
def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the rules of the game."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    print("Welcome to Rock-Paper-Scissors!")
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        # Get player's choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get computer's choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win this round!")
            player_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        # Display current scores
        print(f"Score: You {player_score} - {computer_score} Computer")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Score: You {player_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    play_game()