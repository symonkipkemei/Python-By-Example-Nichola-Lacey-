'''
012
Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.
'''


num1 = int(input("insert your first number: "))
num2 = int(input("insert your second number: "))

if num1 > num2:
    print(num2, "followed by",num1)
else : print(num1, "followed by",num2)


'''
013
Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.
'''

numA = int(input("enter a number that is under 20: "))

if numA >= 20:
    print("Too high")

else:print("Thank you")



'''
014
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”
'''

numB = int(input("enter a number between 10 and 20: "))

if numB >= 10 and numB <= 20:
    print("Thank you.")
else:
    print("incorrect answer")


'''
015
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
'''



color = input("enter your favorite colour: ")
color = str.lower(color)

if color == "red":
    print("I like red too")
else:
    print("I don't like",color, ", I prefer red")

'''
016
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.
'''


rain = str.lower(input("Is it raining(yes/no): "))
if rain == "yes":
    windy = str.lower(input("Is it windy(yes/no): "))
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    "enjoy your day"

'''
017
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trickor-Treating”
'''


userAge = int(input("What is your age?: "))

if userAge >= 18:
    print("you can vote")
elif userAge == 17:
    print("you can learn to drive")
elif userAge == 16:
    print("you can buy a lottery ticket")

else:
    print("You can go Trickor-treating")



'''
018
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
'''

numC = int(input("enter a number: "))

if numC < 10:
    print("too low")
elif numC >= 10 and numC <= 20:
    print("Correct ")

else:
    print("Too high")


'''
019
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
'''

numD = int(input("enter 1 , 2 or 3: "))
if numD == 1:
    print("Thank you")
elif numD == 2:
    print("well done")
elif numD == 3:
    print("correct")
else:
    print("sorry,you entered an invalid number")
