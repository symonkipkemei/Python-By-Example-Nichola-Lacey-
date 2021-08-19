# We will continue from where we last stopped
# we are going to open and read the contents of the books csv file just to remind ourselves
# where we left from

# we first have to import csv

import csv



'''
114
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.
'''

# interesting
# this means we have to retrieve data from the last column of each row .
# and compare if it meets the condition.




file = open("Books.csv", "r")
# converting csv into an iterable
reader = csv.reader(file)

#printing

print("Hello, the following books are present in my repository: ")
# listing the iterables
books = list(reader)
for oneBook in books:
    print(oneBook)

# input
print("\nI will be displaying all the books \nwithin the range of the years you decide.\n")
startYear = int(input("Please input a starting year: "))
endYear = int(input("Please input a ending year:"))

# establishing the range between the user choices
x = range(startYear, endYear)
for row in books:
    if int(row[2]) in range(startYear, endYear):
        print(row[0])

