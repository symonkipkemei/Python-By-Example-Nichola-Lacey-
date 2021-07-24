simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
print(simple_array)

# just like any index, rows and columns starts from 0

'''
096
Create the following using a
simple 2D list using the
standard Python indexing:
'''

listA = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(listA)


'''
097
Using the 2D list from program 096, ask the user to
select a row and a column and display that value
'''

userRow = int(input("Select a row: "))
userColumn = int(input("Select a column: "))
print(listA[userRow][userColumn])


''''
098
Using the 2D list from program 096, ask the user
which row they would like displayed and display
just that row. Ask them to enter a new value and
add it to the end of the row and display the row
again.

'''

userRowDisplayed = int(input("Which row would you like displayed? : "))
print(listA[userRowDisplayed])

newValue = int(input("Please enter a new value: "))

# you first identify the row you want before you append
listA[userRowDisplayed].append(newValue)
print(listA[userRowDisplayed])


'''
099
Change your previous program
to ask the user which row they
want displayed. Display that
row. Ask which column in that
row they want displayed and
display the value that is held
there. Ask the user if they want
to change the value. If they do,
ask for a new value and change
the data. Finally, display the
whole row again

'''

userRowDisplayed = int(input("Which row would you like displayed? : "))
print(listA[userRowDisplayed])
userColumnDisplayed = int(input("Which column would you like displayed? : "))
print(listA[userRowDisplayed][userColumnDisplayed])

changeValue = input("Do you want to change the value (y)es or (n)o : ")
newValue = int(input("What is the new value: "))
if changeValue == "y":
    listA[userRowDisplayed][userColumnDisplayed] = newValue

print(listA[userRowDisplayed])

