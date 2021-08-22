# Just a reminder
# we have different categories of su programs as per my own classification.
# They are:
# 1. Go getters.
# 2. Consumers that depend on Go Getters
# 3. The compilers whom provides a platform for exchange of information between the Go getter and the Consumers


'''
120
Display the following menu to the user:
If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.
If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.
If they do not select a relevant option on the first menu
you should display a suitable message.
'''

# displaying menu to the user
print("(1) Addition\n"
      "(2) Subtraction")
userInput = int(input("Enter 1 0r 2 : "))


# SUB PROGRAM A (Go getters)
# Generate two random numbers btw 5 and 20
# Generate an addition question for the user
# get user answer of the question
# Return userAnswer and correct answer


def addition():
    import random
    numA = random.randint(5, 20)
    numB = random.randint(5, 20)
    correctAnsAdd = numA + numB
    userAnsAdd = int(input(str(numA) + "+" + str(numB) + "= :"))
    ansAdd = (correctAnsAdd, userAnsAdd)
    # Return function can only return one value, we therefore store it in a tuple
    return ansAdd


def subtraction():
    import random
    numA = random.randint(25, 50)
    numB = random.randint(1, 25)
    correctAnsSub = numA - numB
    userAnsSub = int(input(str(numA) + "-" + str(numB) + "= :"))
    ansSub = (correctAnsSub, userAnsSub)
    return ansSub


# SUB PROGRAMME B (The consumer)
# receives variables from other programmes and works them out

def check(userAns, correctAns):
    if userAns == correctAns:
        print("Correct")
    else:
        print("Incorrect, the answer is", correctAns)


# SUB PROGRAMME B (The compiler)

def main():
    if userInput == 1:
        correctAnsSub, userAnsSub = addition()
        check(userAnsSub, correctAnsSub)
    elif userInput == 2:
        correctAnsSub, userAnsSub = subtraction()
        check(userAnsSub, correctAnsSub)
    else:
        print("You entered a wrong input.")

main()