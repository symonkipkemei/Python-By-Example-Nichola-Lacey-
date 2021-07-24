from array import *
# when storing numbers in arrays unlike lists and dictionaries,
# you need to import the array first


num = ["i", 345, 678, 987, 6768]
# above is a list with more than one data type
print(num)
# when declaring an array,
# you first mention the array function followed by
# type of number followed by a list of numbers to be stored"
num = array("i", [688, 890, 789, 564, 7865, 3426, 6787])
print(num)

for x in num:
    print(x)

'''
093
Ask the user to enter five
numbers. Sort them into order
and present them to the user.
Ask them to select one of the
numbers. Remove it from the
original array and save it in a
new array.
'''
originalArray = array("i", [])
for x in range(0, 5):
    userNum = int(input("Enter five numbers: "))
    originalArray.append(userNum)

print(sorted(originalArray))

selectUser = int(input("Please select a one of the numbers"))

originalArray.remove(selectUser)

newArray = array("i", [])
newArray.append(selectUser)

print(originalArray)
print(newArray)

'''
094
Display an array of five
numbers. Ask the user to
select one of the numbers.
Once they have selected a
number, display the
position of that item in the
array. If they enter
something that is not in
the array, ask them to try
again until they select a
relevant item.
'''


# display an array

# select one of the numbers

# display  position of that number
# try again until they select sth that is relevant

from array import *
myArray = array("i", [57, 677, 3756, 58, 56])
correct = False
while not correct:
    print(myArray)
    userSelect = int(input("select one of the numbers  displayed above: "))
    if userSelect in myArray:
        print("The item you selected is in position", myArray.index(userSelect))
        correct = True
    else:
        print('please try again')
        correct = False
'''
095
Create an array of five numbers
between 10 and 100 which each have
two decimal places. Ask the user to
enter a whole number between 2 and 5.
If they enter something outside of that
range, display a suitable error message
and ask them to try again until they
enter a valid amount. Divide each of the
numbers in the array by the number the
user entered and display the answers
shown to two decimal places.

'''

from array import *


# create an array
myArray = array("f", [57.78, 677.98, 3756.45, 58.32, 56.54])

# user to enter a whole number
# suitable error msg if condition not met
# try again


correct = False
ans = 0
while not correct:
    userWhole = int(input("Enter a whole number between 2 and 5 : "))

    if 2 < userWhole < 5:
        print("I love symon")
        for x in myArray:
            ans = x/userWhole
            print(ans.__round__(2))
        correct = True
    else:
        print("please try again")
        correct = False

