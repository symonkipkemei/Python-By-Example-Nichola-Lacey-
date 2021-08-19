'''

115
Using the Books.csv file, display the data in
the file along with the row number of each
'''

# we will try to use loop through a iterable csv and enumerate each row
import csv
file = open("Books.csv", "r")
# converting csv into an iterable
reader = csv.reader(file)
# listing the iterables
books = list(reader)

for index, chapter in enumerate(books):
    print("No", index, chapter)


