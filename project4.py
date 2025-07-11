import random

options = ["rock","paper","scissors"]

while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == "exit":
        print("thanks for playing")
        break
    
    if user_choice not in options:
        print("invalid choice.")
        continue
    
    computer_choice = random.choice(options)
    print(f"computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("it;s a tie")
        
    elif (
        (user_choice == "rock" and computer_choice == "scissors")or
        (user_choice == "paper" and computer_choice == "rock")or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("you win!")
        
    else:
        print("computer wins")
        
        
        
        
        
        