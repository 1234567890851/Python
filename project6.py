questions = {
    "What is the capital of India? ": "delhi",
    "What is 5 + 7? ": "12",
    "Who wrote 'Harry Potter'? ": "jk rowling",
    "What color do you get when you mix red and blue? ": "purple",
    "How many days are there in a week? ": "7"
}

score = 0

for question, correct_answer in questions.items():
    user_answer = input(question).lower()
    
    if user_answer == correct_answer:
        print("correct")
        score += 1
    else:
        print(f"wrong. the correct is: {correct_answer}")
    
print(f"\n you got {score} out of {len(questions)} correct!")