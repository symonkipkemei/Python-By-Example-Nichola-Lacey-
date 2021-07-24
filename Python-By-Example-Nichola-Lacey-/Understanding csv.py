# you first have to import the csv libraries
import csv


# just like text or any other external file , you first have to open the file
# we can assign the open file to a variable for ease of reference
file = open("testing.csv", "w")

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

file.close()