import random 
def Rock_game():
    game = ["rock", "paper", "scissors"]

    while True:
        player_input = input("Enter (Rock, Paper, Scissors): ").lower()
        
        while player_input not in game:
            print("Invalid choice! Please enter Rock, Paper, or Scissors.")
            player_input = input("Enter (Rock, Paper, Scissors): ").lower()

        computer = random.choice(game)
        print(f"Computer: {computer}")

        if (player_input == "rock" and computer == "scissors") or \
        (player_input == "paper" and computer == "rock") or \
        (player_input == "scissors" and computer == "paper"):
            print("--------- You WIN! ---------")

        elif player_input == computer:
            print("----------- Tie! -----------")

        else:
            print("--------- You Lose! ---------")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
if __name__ =="__main__":
 Rock_game()