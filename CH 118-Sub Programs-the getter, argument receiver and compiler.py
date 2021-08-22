'''
118
Define a subprogram that will ask the user to
enter a number and save it as the variable
“num”. Define another subprogram that will
use “num” and count from 1 to that number.
'''


# PROGRAM 1: Get user data

def getUser():
    num = int(input("Enter a number: "))
    return num


# PROGRAM 2 : A program to use num and count from 1 to that number

def count(num):
    for x in range(1, (num + 1)):
        print(x)
# PROGRAM 3 : Main program that compiles the code

def main():
    num = getUser()
    count(num)


main()