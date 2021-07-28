'''
116
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
'''
import csv

file = open("Books.csv", "r")
rowBooks = list(csv.reader(file))

tmp = []

print("The following database contains the following ", len(rowBooks), "publications,\nGo through each and make "
                                                                       "your necessary "
                                                                       "changes.")
# loop through the entire database

for index, row in enumerate(rowBooks):
    print("Would you like too change ", index, "-", row, "?")
    rowChange = input("(Y)es or (N)o:  ")
    rowChange = rowChange.upper()

    if rowChange == "Y":

        change = input("which column would you like to change (T)itle, (Y)ear, (A)uthor? :")
        change = change.upper()
        if change == "T":
            titleChange = str(input("What is your new title? : "))
            newData = titleChange + "," + row[1] + "," + row[2] + "\n"
            tmp.append(newData)
        elif change == "Y":
            yearChange = str(input("What is the year of publishing? :  "))
            newData = row[0] + "," + row[1] + "," + yearChange + "\n"
            tmp.append(newData)

        elif change == "A":
            authorChange = str(input("What is the name of the author? : "))
            newData = row[0] + "," + authorChange + "," + row[2] + "\n"
            tmp.append(newData)

        else:
            print("wrong input")

    elif rowChange == "N":
        data = row[0] + "," + row[1] + "," + row[2] + "\n"
        tmp.append(data)
    else:
        print("wrong data input")

# confirm if everything is well appended to the list
for row in tmp:
    print(row)

# lets now append the changes to our csv database
# by overriding the existing list with the new changes
# we will use "w" to completely override the list

file = open("Books.csv", "w")
for row in tmp:
    file.write(row)
file.close()


# reading the csv file we just appended

file = open("Books.csv", "r")
for row in file:
    print(row)
