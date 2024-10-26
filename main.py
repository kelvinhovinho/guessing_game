def new_gamae():
    
    guessess = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-"*13)
        print(key)

        for i in options[question_num]:
            print(i)

        guess = input("Enter A,B,C or D: ").upper()
        guessess.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

        question_num+=1
    
    display_score(correct_guesses, guessess)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guessess):
    print("-"*13)
    print("RESULTS")
    print("-"*13)

    print("Answers ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")

    print("Guesses ", end="")
    for i in guessess:
        print(i, end= " ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is: {score}%")
    
def play_again():
    response = input("Do you want to play again? yes/no: ").lower()

    if response == 'yes':
        return True
    else:
        return False

questions = {
    "1. Who created python?":"A",
    "2. When was Python created?":"B",
    "3. Python is distributed to which commedy group?":"C",
    "4. Is the earth round?":"A"
}

options =[
    ["A. Guido van Rossam","B. Elon Musk","C. Bill Gates","D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991","C. 2000","D. 2016"],
    ["A. Lonely Island","B. Smosh", "C. Monty Python","D. snl"],
    ["A. True", "B. False","C. Sometimes", "D. What's Earth?"]
    ]


new_gamae()

while play_again():
    new_gamae()

print('BYEEEEE!!!')