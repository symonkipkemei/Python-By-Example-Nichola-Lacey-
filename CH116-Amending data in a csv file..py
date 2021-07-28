# We are going to test our skills on amending data in a csv file.
# Remember we can only append a csv file with new data
# but we cannot re-write a particular data in the csv

'''
116
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
'''

# open books.csv file and read

file = open("Books.csv", "r")

# use csv reader to convert rows in books into iterables
import csv

reader = csv.reader(file)

# List the iterables using the list constructor

bookRows = list(reader)
# display list to user
for rows, index in enumerate(bookRows):
    print("No", rows, "-", index)


# deleting a row
delRow = int(input("which row number would you like to delete: "))
del bookRows[delRow]

# display the list again

for rows, index in enumerate(bookRows):
    print("No", rows, "-", index)

# create a tmp list
# in order to alter the list

tmp = []
for row in bookRows:
    tmp.append(row)

print(tmp)

# altering data in a list



