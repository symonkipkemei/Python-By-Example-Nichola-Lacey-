# you first have to import the csv libraries
import csv


# just like text or any other external file , you first have to open the file
# we can assign the open file to a variable for ease of reference
file = open("testing.csv", "a")

# Writing to a csv file

info = input("please insert what do you do when in siege?: ")
whatDo = input("Do you smell success or failure?:  ")
plan = input("what are you planning to do about school work?: ")

# we are going to write the above information into a csv file
# we need the variables , commas and line break

newRecord = info + "," + whatDo + "," + plan + "\n"

# writing to the csv file we created
file.write(newRecord)


# close the file
file.close()


# reading what is in the file

file = open("testing.csv", "r")

x = file.read()
print(x)
print("Let's try displaying this information differently\n")
file.close()

# TRYING PRINTING WITH LOOP
# the code below loops through each row and print each individually

file = open("testing.csv", "r")
for y in file:
    print(y)
file.close()


# EXPLORING THE ATTRIBUTE CSV READER
# we have already understood how to write a string and variables to a a csv file
# let us now evplore how to read a csv file

file = open("testing.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()


# why csv reader and not  file.read?

# the difference is
# file.read will just print each individual row separated by  commas
# csv reader converts each row into an iterable , specifically a list.
# Therefore we can access each column individually!

#   ALTERNATIVELY

# instead of reading a file with loop we can convert it to a list  using a list constructor

file = open("testing.csv", "r")
reader = csv.reader(file)
row = list(reader)
print(row)
# Bombooclat!
# listing the iterable converts it into a 2d list
print(row[0])
print(row[0][1])
file.close()



# SEARCHING FOR A FILE INA CSV

# let's open the file first
file = open("testing.csv", "r")
#input your search file
searchItem = input("Insert an item you would like to search?: ")

# list all rows and seach if item is in the rows
# This does not need a csv reader to convert it into an iterable
for row in file:
    if searchItem in row:
        print(row)


