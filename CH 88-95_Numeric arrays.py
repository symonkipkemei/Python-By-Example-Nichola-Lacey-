'''
088
Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order.

'''


#IMPORTS
import random
from array import *
#

numArray = array("i", [])

for x in range(0,5):
    num = int(input("Enter an integer: "))
    numArray.append(num)

# sorting array into ascending order
# reversing array
numArray = sorted(numArray)
numArray.reverse()
print(numArray)


'''
089
Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).
'''


arrayStore = array("i", [])

for x in range(0, 5):
    num = random.randint(0, 999)
    arrayStore.append(num)

for z in arrayStore:
    print(z)


'''
090
Ask the user to enter numbers. If they enter a
number between 10 and 20, save it in the array,
otherwise display the message “Outside the
range”. Once five numbers have been
successfully added, display the message “Thank
you” and display the array with each item shown
on a separate line.
'''

numArray = array("i", [])

count = 0

while count < 5:
    userNum = int(input("enter a number between 10 and 20: "))
    if 10 < userNum < 20:
        numArray.append(userNum)
        count += 1
    else:
        print("Outside the range")

print("thank you")
for r in numArray:
    print(r)


'''
091
Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
092 appears in the list.
'''

arrayz = array("i", [34, 34, 5, 78, 98])
print(arrayz)
chosenNum = int(input("Enter one of the numbers from the array:"))
print(chosenNum, "appears", arrayz.count(chosenNum), "times")

'''
092 appears in the list.
Create two arrays (one
containing three numbers that
the user enters and one
containing a set of five random
numbers). Join these two arrays
together into one large array.
Sort this large array and display
it so that each number appears
on a separate line.

'''

array1 = array("i", [])
array2 = array("i", [])


for x in range(0, 3):
    userNum = int(input("please enter a number: "))
    array1.append(userNum)

for y in range(0,5):
    randomNum = random.randint(0, 999)
    array2.append(randomNum)

array1.extend(array2)

print(array1)
array1= sorted(array1)
for w in array1:
    print(w)