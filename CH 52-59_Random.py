import random

'''
052
Display a
random
integer
between
1 and 100
inclusive.
'''

#integer

num = random.randint(1, 100)
print(num)


'''
053
Display a
random
fruit from
a list of
five fruits
'''

fruits = ["Oranges", "Watermelon", "Avocado", "Pineapple", "Banana"]
print(random.choice(fruits))


'''
054
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails

'''

# use random choice to choose between h or t
choice = ["h", "t"]
computerChoice = random.choice(choice)
# ask user for his/her choice
userOption = input("Hello, make a choice between heads or tail (h/t): ")
# check if user is same as computer's choice
# display you win
# if not ,display you loose
# display what computer selected
if userOption == computerChoice:
    print("You win")
else:
    print("Bad luck")

print("the computer selected", computerChoice)


'''
055
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.
'''

# create a random num  using random.randit (1,5)
ranNum = random.randint(1, 5)
# ask user to pick number
userNum = int(input("please input a number:"))
# if usernum is equal to random num, print message well done
# else if usernum is greater than random num, print too high and vice versa
# ask for a second number
# if they guess correctly on their second guess,display correct otherwise you loose

if userNum == ranNum:
    print("well done")
elif userNum > ranNum:
    print("too high")
elif userNum < ranNum:
    print("too low")

secondNum = int(input("please input your second choice:"))
if secondNum == ranNum:
    print("correct")
else:
    print("you loose")


'''
056
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.
'''

'''
057
Update
program 056
so that it
tells the
user if they
are too high
or too low
before they
pick again

'''

print('''
Let\'s compete between the computer and you and see
if you stand a chance of picking the same number
randomly picked by the computer\n''')
wholeNum = random.randint(1, 10)
userNum = int(input("please input a number:"))
while userNum != wholeNum:
    userNum = int(input("please insert another number:"))
    if userNum < wholeNum:
        print("too low")
    else:
        print("too high")
else:
    print("you picked the correct number")

