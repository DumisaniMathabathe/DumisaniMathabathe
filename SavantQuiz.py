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
    "Who is the president of the Republic of South Africa?": "Cyril Ramaphosa",
    "Which country has the highest life expectancy?": "Hong Kong",
    "What is the most common surname in the United States?": "Smith",
    "Who was the Ancient Greek God of the Sun?": "Apollo",
    "How many minutes are in a full week?": 10080,
    "Aureolin is a shade of what color?": "Yellow",
    "How many faces does a Dodecahedron have?": 12,
    "What is the 4th letter of the Greek alphabet?": "Delta",
    "What company was initially known as Blue Ribbon Sports?": "Nike",
    "What art form is described as decorative handwriting or handwritten lettering?": "Calligraphy",
    "What software company is headquartered in Redmond, Washington?": "Microsoft",
    "How many dots appear on a pair of dice?": 42,
    "What is acrophobia a fear of?": "Heights",
    "December 26 is known by what names in Ireland?": "Saint Stephen's Day",
    "What phone company produced the 3310?": "Nokia",
    "What is the world’s largest retailer?": "Walmart",
    "Which day of the week does the Jewish Sabbath begin?": "Friday",
    "What is a word, phrase, number, or other sequence of characters that reads the same backward as forward?": "Palindrome",
    "What is the name of the Chinese philosophical system that emphasizes harmony with nature?": "Taoism",
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
