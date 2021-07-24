print("Hello World .This is the beginning of my story")

'''
001-Ask for the user’s first name and
display the output message
'''

userName= input("Hello, please insert your nickname here: ")
print("Hello", userName,"!\nWelcome to my world.I hope you love coding too!")


'''
002
Ask for the user’s first name and then ask for
their surname and display the output message
Hello [First Name] [Surname]
'''

userFirstName= input("Hello, please insert your first name here: ")
userSecondName= input("Hello, please insert your second name here: ")
print("Hello [",userFirstName, "] [", userSecondName,"]")


'''
003
Write code that will display the joke “What do you call a bear with no
teeth?” and on the next line display the answer “A gummy bear!” Try to
create it using only one line of code
'''

print("What do you call a bear with no teeth? \nA gummy bear!")


'''
004
Ask the user to enter
two numbers. Add
them together and
display the answer as
The total is
[answer].
'''

try:
    num1 = int(input("Hello again, please insert your first number here: "))
    num2 = int(input("Hello once more, please insert your second number here: "))
    ans = num1 + num2
    print("The total answer is [", ans, "]")
except ValueError:
    print("Its funny how you cannot distinguish numbers from text\nplease try again", userName)


'''
005
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer].
'''

try:
    anum1 = int(input("Insert your first number: "))
    anum2 = int(input("Insert your second number: "))
    anum3 = int(input("Insert your third number: "))

    addans = anum1 + anum2
    overalans = addans * anum3
    print("The total answer is [", overalans, "]")

except ValueError:
    print("It seems you will have to go to nursery school once more\nplease try again", userName)


'''
006
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a userfriendly format
'''

try:
    pizzaStart = int(input("Hello, how many slices of pizza did you start with?: "))
    pizzaEaten = int(input("Hello, how many slices of pizza have you eaten?: "))
    pizzaLeft=pizzaStart-pizzaEaten
    print("You have", pizzaLeft, "left.Please eat slowly.")


except ValueError:
    print("It seems you are overfeeding\nplease try again", userName)


'''
007
Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age].
'''



try:
    userName = input("Hello, what is your name please: ")
    age = int(input("What is your age?: "))
    #the input function can only support one argument ( a string and not a variable)

    nextBirthday = age+1
    print( userName, "next birthday you will be", nextBirthday)


except ValueError:
    print("It is sad that you do not remember yourself\nplease try again", userName)


'''
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay
'''

billPrice = int(input("Hello, what is the total price of the bill: "))
dinners = int(input("How many dinners are there?: "))

eachDinnerPay = billPrice/dinners
print("Each dinner will pay", eachDinnerPay)



'''
009
Write a program
that will ask for a
number of days
and then will
show how many
hours, minutes
and seconds are
in that number of
days.
'''

numofDays = int(input("Hello, How many days are there to final architecture pin up?: "))
hours = 24*numofDays
minutes = hours*60
seconds = minutes*60

print("There are,\n", hours, "hours\n", minutes, "minutes\n", seconds, "seconds\n in ", numofDays, "number of days to final year pin up")

'''
010
There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
'''

weightInKg = int(input("Enter your weight in kilograms: "))
weightInPound = weightInKg * 2204
print("You are weighing ", weightInPound, "pounds")

'''
011
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.
'''

numA = int(input("Enter a number over 100: "))
numB = int(input("Enter a number under 10: "))
numOfTimes=numA//numB
print("The smaller number goes into the bigger number", numOfTimes, "times")


