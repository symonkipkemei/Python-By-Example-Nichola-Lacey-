"""" Create an SQL database called PhoneBook that
contains a table called Names with the following data:"""

# first step is to  import the sql library
import sqlite3
import random

# create a database called PhoneBook

with sqlite3.connect("PhoneBook.db") as db:
    # create an object called cursor
    cursor = db.cursor()

# creating a table using the object
# ensure the values within the table are separated with a comma

cursor.execute("CREATE TABLE IF NOT EXISTS phonebook(ID integer PRIMARY KEY,"
               "FirstName text NOT NULL,"
               "Surname text NOT NULL,"
               "PhoneNumber integer)")

db.commit()

for y in range(0, 5):
    correct = False
    while not correct:
        try:
            Id = int(input("Insert ID: "))
            FirstName = input("Insert first name: ")
            SecondName = input("Insert second name: ")
            PhoneNo = int(input("Insert phone no: "))

            # saving into database
            cursor.execute("INSERT INTO phonebook(ID,FirstName,Surname,PhoneNumber )"
                           "VALUES(?,?,?,?)", (Id, FirstName, SecondName, PhoneNo))
            correct = True

        except ValueError:
            print("You are sleepy.Wrong value, try again")

        except sqlite3.IntegrityError:
            print("Data already exists in database, try a different one.")

# save and close the database
db.commit()
db.close()
