# Define the quiz questions and answers
quiz_data = {
    "What is the capital of France?": "Paris",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the square root of 64?": "8",
    "What is the chemical symbol for water?": "H2O",
    "Which planet is known as the Red Planet?": "Mars",
    "How many continents do we have?": "7",
    "Who was South Africa's first black President?": "Nelson Mandela",
    "Who drew 'The Mona Lisa'?": "Leonardo DaVinci",
    "Who is the president of the Republic of South Africa?": "Cyril Ramaphosa"
}

# Function to run the quiz
def run_quiz():
    score = 0
    total_questions = len(quiz_data)
    
    # Loop through each question
    for question, answer in quiz_data.items():
        print(question)
        user_answer = input("Your answer: ").strip()
        
        # Check if the user's answer is correct
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answer}\n")
    
    # Display the final score
    print(f"You got {score} out of {total_questions} questions right!")

# Run the quiz
run_quiz()