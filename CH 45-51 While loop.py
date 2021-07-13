
'''
045
Set the total to 0 to start with. While the total is 50 or less, ask
the user to input a number. Add that number to the total and
print the message “The total is… [total]”. Stop the loop when
the total is over 50

'''


total = 0
while total < 50:
    num = int(input("Please input a number"))
    total += num
    print("The total is [", total, "]")


'''
046
Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program.
'''


userNum = 0
while userNum <= 5:
    userNum = int(input("please input a number: "))
else:
    print("The last number you entered was", userNum)

'''
047
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.
'''

# you have to set the variable that you have to test if their conditions are being met
# then ask the same while you are within the code
# As long as the condition is being met the while loops through its codes

userNum = int(input("please input a number: "))
userFeedback = "y"
total1 = userNum
while userFeedback == "y":
    userAnother = int(input("please enter another number: "))
    total1 += userAnother
    userFeedback = input("Do you want to add another number? (y/n): ")
else:
    print(total1)


'''
048
Ask for the name of somebody the user wants to invite
o a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
hey want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party
'''

# ask for the name of the invitee
# display a nice message that he has been invited
# create the question variable that controls the while loop .Call it shouldInvite


shouldInvite = "y"
attendees = 0


while shouldInvite == "y":
    inviteeName = input("please insert invitee\'s name: ")
    attendees += 1
    shouldInvite = input("Do you want to invite another person? (y/n): ")

else:
    print(attendees)

'''
049
Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”
'''


# create variable compnum
compnum = 50

# user to enter a number
print('''
Welcome to the guess game
Guess a number until you enter it correctly \n''')
userNo = int(input("please insert your first guess: "))
# if lower than compnum tell them guess to too low
# if higher  than compnum tell them guess too high
# if they enter the compnum,display well done message
# compnum is our loop condition
count = 1
while compnum != userNo:
    if userNo < compnum:
        print("Your guess is too low")
    else:
        print("your guess is too high")
    count += 1
    userNo = int(input("please enter another guess:"))

else:
    print("well done, you took", count, "attempts")

'''
050
Ask the user to enter a number between
10 and 20. If they enter a value under 10,
display the message “Too low” and ask
them to try again. If they enter a value
above 20, display the message “Too high”
and ask them to try again. Keep repeating
this until they enter a value that is
between 10 and 20 and then display the
message “Thank you”

'''
# I think , I need a function that asks the user to please input a number
# the repetitions are becoming boring
# ask a number from the user
userNum = int(input("please input a number: "))
# set a condition statement using both logical and comparison indicators

while 20 >= userNum >= 10:
    if userNum < 10:
        print("Too low")
    else:
        print("Too high")
    userNum = int(input("please input a number: "))
else:
    print('Thank you')

'''
051
Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly, display the
message “No, try again” until they get it right. When the number of green bottles gets
down to 0, display the message “There are no more green bottles hanging on the wall”
'''

totalBottles = 10


while totalBottles > 0:
    print("There are ", totalBottles, "green bottles hanging on the wall,\n"
                                      "and if 1 green bottle should accidentally fall,\n ")
    userAns = int(input("How many green bottles will be hanging on the wall? :"))
    remBottles = totalBottles - 1

    if userAns != remBottles:
        print("No, try again")
    else:
        print("There will be", remBottles, "green bottles hanging on the world")
        totalBottles = remBottles
else:
    print("There are no more green bottles hanging on the wall\n")
