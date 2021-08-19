'''
117
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything
'''

# INTRO

import random
import csv

print("Hello, Welcome to the Math game!\n"
      "You will be asked two random questions\n"
      "I will be looking forward to your answers!\n")

file = open("MathsQuiz.csv", "a")

userName = input("What is your name?: ")

# QUESTIONS
# Question 1
quizInteger1 = random.randint(1, 20)
quizInteger2 = random.randint(1, 10)
quiz1Ans = quizInteger1 * quizInteger2
quiz1 = str(quizInteger1) + "*" + str(quizInteger2) + "="

print(quiz1)
userAns1 = int(input("Input your answer: "))

# Question 2
quizInteger1 = random.randint(1, 20)
quizInteger2 = random.randint(1, 10)
quiz2Ans = quizInteger1 + quizInteger2
quiz2 = str(quizInteger1) + "+" + str(quizInteger2) + "="

print(quiz2)
userAns2 = int(input("Input your answer: "))

# STORING DATA IN A CSV FILE


record = userName + "," + str(quiz1) + "," + str(quiz2) + "," + str(quiz1Ans) + "," + str(quiz2Ans) + "," + str(
    userAns1) + "," + str(userAns2) + "\n"

file.write(record)
file.close()
