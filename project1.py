import random

# Step 1: Generate random number
secret_number = random.randint(1, 10)

# Step 2: Ask user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Step 3: Check guess
if guess == secret_number:
    print("🎉 You guessed it right!")
else:
    print(f"❌ Wrong! The number was {secret_number}")
