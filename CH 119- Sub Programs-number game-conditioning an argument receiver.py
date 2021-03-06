'''
119
Define a subprogram that will ask the user to
pick a low and a high number, and then
generate a random number between those
two values and store it in a variable called
“comp_num”.

Define another subprogram that will
give the instruction “I am thinking of a number…”
and then ask the user to guess the number they
are thinking of.

Define a third subprogram that will check to see if the
comp_num is the same as the user’s guess. If it
is, it should display the message “Correct, you
win”, otherwise it should keep looping, telling the
user if they are too low or too high and asking them
to guess again until they guess correctly
'''


# PROGRAM 1: picking high and low number from the user (Go Getter)

def getUser():
    import random
    lowNum = int(input("Enter a low number: "))
    highNum = int(input("Enter a high number: "))
    compNum = random.randint(lowNum, highNum)
    return compNum


# PROGRAM 2: User trying to guess my numbers (Go getter)

def guess():
    userGuess = int(input("I am thinking of a number\n"
                          "Guess the number am thinking of: "))
    return userGuess


# PROGRAM 3: (The consumer/the argument receiver) check if user guess is same as computer guess
# all conditional statements are run through this sub programme

def checkIfGuess(compNum, userGuess):
    correct = False
    while not correct:
        if compNum == userGuess:
            print("Correct, you guessed correctly")
            correct = True
        elif userGuess > compNum:
            print("Too High")
            userGuess = int(input("Guess the number am thinking of again: "))
            # acts as a mediator between a continuous loop and new user answer
        elif userGuess < compNum:
            print("Too low")
            userGuess = int(input("Guess the number am thinking of again: "))


# PROGRAM 4: (The connector) loops through and connects variables from different programs.
# this is the heart of the project whereas the consumer is the brain of the project.

def main():
    compNum = getUser()
    userGuess = guess()
    checkIfGuess(compNum, userGuess)


# The rule of thumb is that the main programme is only a compiler .
# Therefore, sort all your relations at the go getter and the argument receiver level.

main()
