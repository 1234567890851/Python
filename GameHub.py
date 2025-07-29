import RockPaperScissor
import GuessingNumbergame
import HangingMan
print("----------------------------- Hello Gamer -------------------------------------")
print("************Which Game U Want to Play ?*****************")
print("1.Number Guess Game.")
print("2.Rock Paper Scissor.")
print("3.Hangman game .")

user_input = int(input("Enter Your Option (1-3):"))

if user_input == 1:
 print("-----------NICE CHOICE ------------")
 print("Lets Play")
 GuessingNumbergame.Guess_Game()

elif user_input==2:
  print("-----------NICE CHOICE ------------")
  print("Lets Play")
  RockPaperScissor.Rock_game()

elif user_input==3:
  print("-----------NICE CHOICE ------------")
  print("Lets Play")
  HangingMan.hangman()
else:
  print("Enter A valid Input !") 

#heere u see why i us eif main == name 