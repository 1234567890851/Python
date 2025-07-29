import random
def Guess_Game():
   Highest_num = 100
   Lowest_num = 1
   rand =(random.randint(Lowest_num,Highest_num))
   guesess=0
   is_running = True
   guess=int(input("Enter Your Guess Number :"))
   guesess+=1
   while is_running:
      if rand > guess:
         print("Think About Gretest Number")
         guess=int(input(""))
         guesess+=1
   
      elif rand < guess:
         print("Think About Lowest Number")
         guess=int(input(""))
         guesess+=1
      else:
         print("You Guess The Random nunber ")
         is_running = False
   print("---------------------------------------------")
   print(f"You Guess The Random Number {rand} IN {guesess} guesess")
 
if __name__=="__main__":
 Guess_Game()