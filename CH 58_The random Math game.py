'''
  058
Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five
'''

import random

# create a variable to store the user's marks
marks = 0

# create the opening statement for the math game

print(''' This is a math game that is going to generate random quizzes for you.
The total number of quizzes are 5.
please attempt all.You will be awarded marks at the end''')

# use for loop to repeat the question 5 times and its resultant outcomes
# the random option has to be within the for loop so that it can generate new possible outcomes
for x in range(0, 5):
    # create random numbers ranging frm 1 to 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # use string concatenation to create 5 random quizzes

    quiz1 = str(num1) + "+" + str(num2) + "= :"
    quiz2 = str(num1) + "*" + str(num2) + "= :"
    quiz3 = str(num1) + "-" + str(num2) + "= :"
    quiz4 = str(num1) + "/" + str(num2) + "= :"
    quiz5 = str(num1) + "*" + str(num2) + "-" + str(num1) + "= :"

    # create answers for each quizzes

    ans1 = num1 + num2
    ans2 = num1 * num2
    ans3 = num1 - num2
    ans4 = num2 / num1
    ans5 = (num1 * num2) - num1

    # create a list of the quizzes for random choice selection by the computer

    quizzes = [quiz1, quiz2, quiz3, quiz4, quiz5]
    computerQuiz = random.choice(quizzes)

    print(computerQuiz)
    userInput = int(input("please enter your answer :"))

    if computerQuiz == quiz1:
        if ans1 == userInput:
            print("correct!. you have have earned 1 mark")
            marks += 1
        else:
            print("wrong!.try the next quiz")

    elif computerQuiz == quiz2:
        if ans2 == userInput:
            print("correct!. you have have earned 1 mark")
            marks += 1
        else:
            print("wrong!.try the next quiz")

    elif computerQuiz == quiz3:
        if ans3 == userInput:
            print("correct!. you have have earned 1 mark")
            marks += 1
        else:
            print("wrong!.try the next quiz")

    elif computerQuiz == quiz4:
        if ans4 == userInput:
            print("correct!. you have have earned 1 mark")
            marks += 1
        else:
            print("wrong!.try the next quiz")

    elif computerQuiz == quiz5:
        if ans5 == userInput:
            print("correct!. you have have earned 1 mark")
            marks += 1
        else:
            print("wrong!.try the next quiz")

    else:
        print("you entered a wrong value")

print("You got", marks, "out of 5 marks.Congratulations!")
