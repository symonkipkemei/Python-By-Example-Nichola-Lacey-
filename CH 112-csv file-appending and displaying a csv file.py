'''
112
Using the Books.csv file
from program 111, ask
the user to enter another
record and add it to the
end of the file. Display
each row of the .csv file
on a separate line.

'''



import  csv

# appending to the csv file
dataset = open("Books.csv", "a")
print('Enter another set of data')
title = input("Input title of book: ")
author = input("Input name of the author: ")
year = input("Input year of publishing: ")
info = title + "," + author + "," + year + "\n"
dataset.write(str(info))
dataset.close()

# print csv

dataset = open("Books.csv", "r")
print(dataset)
for row in dataset:
    print(row)
dataset.close()

