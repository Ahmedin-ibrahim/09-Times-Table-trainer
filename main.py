
import random
import time

print("WELCOME TO TIMES TABLE TRAINER!")

choice = input("Choose a table (1-15) or type mixed: ")

wrong_answers = []

start_time = time.time()

previous_question = ""

score = 0

for i in range(10):

    if choice == "mixed":
        num1 = random.randint(1, 15)
    else:
        num1 = int(choice)

    num2 = random.randint(1, 15)

    question = str(num1) + " x " + str(num2)

    while question == previous_question:
        num2 = random.randint(1, 15)
        question = str(num1) + " x " + str(num2)

    previous_question = question

    correct_answer = num1 * num2

    print("\nQuestion", i + 1)
    print(question, "= ?")

    try:
        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")
            score = score + 1

        else:
            print("Wrong!")
            wrong_answers.append(
                [question, answer, correct_answer]
            )

    except ValueError:
        print("Please enter a number.")

        wrong_answers.append(
            [question, "Invalid input", correct_answer]
        )

end_time = time.time()

total_time = round(end_time - start_time, 1)

print("\n===== QUIZ RESULTS =====")

print("Your score:", score, "/ 10")
print("Time taken:", total_time, "seconds")

print("\nQuestions to practise:")

if len(wrong_answers) == 0:
    print("Excellent! No mistakes!")

else:
    for mistake in wrong_answers:
        print(mistake[0])
        print("Your answer:", mistake[1])
        print("Correct answer:", mistake[2])
        print("-------------------")

print("Thank you for playing!")