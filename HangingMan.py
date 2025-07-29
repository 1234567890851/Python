import random
def hangman():
  # Step 1: Word list
  words = ["python", "hangman", "apple", "banana", "computer", "laptop", "keyboard"]
  secret_word = random.choice(words)

  # Step 2: Game setup
  guessed_letters = []
  lives = 6

  print("🎮 Welcome to Hangman!")
  print("Guess the word below:")
  print("_ " * len(secret_word))

  # Step 3: Game loop
  while lives > 0:
      guess = input("\n🔤 Enter a letter: ").lower()

      if not guess.isalpha() or len(guess) != 1:
          print("⚠️ Please enter a single alphabet letter only.")
          continue

      if guess in guessed_letters:
          print("🔁 You already guessed that letter.")
          continue

      guessed_letters.append(guess)

      if guess in secret_word:
          print("✅ Good guess!")
      else:
          lives -= 1
          print(f"❌ Wrong guess! Lives left: {lives}")

      # Step 4: Show current word progress
      display_word = ""
      for letter in secret_word:
          if letter in guessed_letters:
              display_word += letter + " "
          else:
              display_word += "_ "
      print("\n" + display_word)

      # Step 5: Win condition
      if "_" not in display_word:
          print("🎉 Congratulations! You guessed the word:", secret_word)
          break

  # Step 6: Lose condition
  if lives == 0:
      print("💀 Game Over! The word was:", secret_word)
if __name__ =="__main__":
  hangman()

# import random 
# words=["mango","apple","banana","coconut","watermelon"]
# guess_word = random.choice(words)
# print(guess_word)
# guess = " _ "*len(guess_word)
# print(guess)
# print("HINT!!,Word Belong TO Fruets")
# print("Start Geussing word")

# user_guess = input("Enter a Word :")
# is_runnig = True
# while is_runnig:
#   if user_guess in guess_word:
#     guess+=user_guess
#     print(guess)
#   else:
#     print("Enter A valid Optoin ")