import math

'''
027
Ask the user to enter a
number with lots of
decimal places. Multiply
this number by two and
display the answer.
'''


num1 = float(input("insert number with lots of decimal points: "))
ans = num1 * 2
print(ans)

'''
028
Update program 027 so that it will display the answer to
two decimal places
'''

ans = round(ans, 2)
print(ans)


'''
29
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places.
'''
# user input above 500
num2 = int(input("insert a integer that is over 500: "))
# square root
sqrtNum = math.sqrt(num2)
# round off
sqrtNum = round(sqrtNum, 2)
# display
print(sqrtNum)


'''
030 
Display pi (π) to five
decimal places.
'''
# display pi
pi = math.pi
# round and display pi
print(round(pi, 5))


'''
031
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).
'''

# input radius from user
radius = int(input("insert radius of circle: "))
# work out area
area = math.pi * (radius ** 2)
# display area

print(str(area) + " meter square")

'''
032
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
'''
# input radius and depth of cylinder
cylinderRadius = int(input("insert radius of cylinder: "))
cylinderDepth = int(input("insert depth of cylinder: "))


# work out volume
# area of cylinder
cylinderArea = math.pi * (cylinderRadius ** 2)
cylinderVolume = cylinderArea * cylinderDepth
# round to 3 decimal points
print(str(round(cylinderVolume, 3)) + " cubic meters")


'''
033
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).
'''

# user input of two numbers
userNum1 = int(input("Enter first number: "))
userNum2 = int(input("Enter second number: "))


# divide first by second number (whole number division)
wholeNum = userNum1//userNum2

# work out modulus
modulusNum = userNum1 % userNum2
# print in user friendly mode
print(str(userNum1) + " divided by " + str(userNum2) + " is " + str(wholeNum) + " with " + str(modulusNum) + " remaining")
# preferred option when writing a sentence with variables containing different data types
print(str(userNum1), "divided by", userNum2, "is", wholeNum, "with", modulusNum, "remaining")

'''
034
Display the following message:
1) Square
2) Triangle

Enter a number:

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
'''

# display user input option message
userOption = input('''
1) Square
2) Triangle

Enter a number:
''')
# if option is 1 ask :
# ask length of one side
# display area
if userOption == "1":
    lengthOfSquare = int(input("Enter the length of one side: "))
    areaOfSquare = lengthOfSquare ** 2
    print(areaOfSquare)

# if option is 2:
# ask for base and height of triangle
# display area
elif userOption == "2":
    baseOfTriangle = int(input("Enter base of triangle: "))
    heightOfTriangle = int(input("Enter height of triangle: "))
    areaOfTriangle = 0.5 * baseOfTriangle * heightOfTriangle
    print(areaOfTriangle)
# display error message if conditions are not met
else:
    print("You entered a wrong input, please try again")



