'''
117
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.
'''

# import modules
import random

print("Hello there, Welcome to the Math game.\n"
      "You will be asked two random math quizes.\n"
      "Please try and attempt.")


# user name
userName = input("what is your name:")
# two random math questions
# QUIZ 1
num1 = random.randint(10,100)
num2 = random.randint(10,100)
quiz1 = "Quiz1: " + str(num1) + "+" + str(num2) + "= : "
quiz1Ans = num1 + num2

# QUIZ 2
num1 = random.randint(10,100)
num2 = random.randint(10,100)
quiz2 = "Quiz1: " + str(num1) + "-" + str(num2) + "= : "
quiz2Ans = num1-num2

print(quiz1)
userAns1 = int(input("please insert your answer:"))
marks = 0
if userAns1 == quiz1Ans:
    marks += 1

print(quiz2)
userAns2 = int(input("please insert your answer:"))
if userAns2 == quiz2Ans:
    marks += 1

print(marks)

# storing data in a csv
# username, quiz 1, quiz 2, answer , marks


storeData = userName + "," + str(quiz1) + "," + str(quiz2) + "," + str(userAns1) + "," + str(userAns2) + "," + str(marks) + "\n"

# create a csv file

file = open("Marks.csv", "a")
file.write(storeData)
file.close()
