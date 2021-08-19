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

# converting csv into an iterable and 2D Listing
books = list(csv.reader(file))

tmp = []
# displaying available books
print("The following database contains the following ", len(books), "publications,\nGo through each and make "
                                                                    "your necessary "
                                                                    "changes.\n")
for index, row in enumerate(books):
    print(index, row)


# DELETING A ROW FROM THE DATABASE

# deleting a row
delRow = int(input("\nwhich row number would you like to delete:"))
del books[delRow]

# display the list again

print("\nRow", str(delRow), "deleted, Below is the new list\n")

for rows, index in enumerate(books):
    print("No", rows, "-", index)

# AMENDING DATA IN A CSV FILE

# loop through the entire database scanning for areas the editor wants to make changes
for index, row in enumerate(books):
    print("\nWould you like too change ", index, "-", row, "?")
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
print("This is to confirm if everything was well appended\n"
      "into our temporary list\n")
for row in tmp:
    print(row)

# let's now close the file we opened to make changes
file.close()


# APPENDING THE CHANGES MADE TO THE CSV FILE

# lets now append the changes to our csv database
# by overriding the existing list with the new changes
# we will use "w" to completely override the list

file = open("Books.csv", "w")
for row in tmp:
    file.write(row)
file.close()

# reading the csv file we just appended

print("Bombooclaat!\n"
      "Below is the list we just ammended the changes\n"
      "Go through it and affirm that all the changes made are consistent to your inputs\n"
      "cheers!")


file = open("Books.csv", "r")
for row in file:
    print(row)
