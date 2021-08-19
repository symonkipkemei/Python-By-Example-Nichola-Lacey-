'''
113
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
'''

# first display the current books csv file.
import csv
file = open("Books.csv", "r")
reader = csv.reader(file)
books = list(reader)

for row in books:
    print(row)
file.close()

# user input on how many more books  they would like to append

userNo = int(input("How many more books would you like to add?: "))
#  ask for an author and display

for x in range(0, userNo):
    file = open("Books.csv", "a")
    title = input("Input title of book: ")
    author = input("Input name of the author: ")
    year = input("Input year of publishing: ")
    newRecord = title + "," + author + "," + year + "\n"
    file.write(str(newRecord))
    file.close()

# asking for an author
file = open("Books.csv", "r")
for x in file:
    print(x)
print("Lets search an author from above data set")
file.close()

file = open("Books.csv", "r")
authorAsk = str(input("Input name of the author: "))
count = 0
for row in file:
    if authorAsk in row:
        print(row)
        count += 1
if count == 0:
    print("Hello dear one, there is no search an author.")
# the count variable summarises all the ..
# no their is no search an author in every row into one statement after the end of the search
file.close()

# An interesting way of imitating while loop
# if this action happens we will add the variable by one
# thus it will stop
# if it does happen it remains 0 and thefore we can assign a message for conditions not met
