import sqlite3

# create a database


with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# CREATE AUTHORS TABLE
# note that the only quote marks are at the beginning and END of the attribute
# double quotes allows it the statement to span over three lines


cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
Name text PRIMARY KEY ,
PlaceofBirth text NOT NULL) ;""")

# CREATE BOOK TABLE
cursor.execute("""CREATE TABLE IF NOT EXISTS Books
(ID integer PRIMARY KEY , 
Title text NOT NULL ,
Author text NOT NULL ,
DatePublished text NOT NULL) ;""")


# known no of values
# known number of parameters


def author():
    """INSERT INTO AUTHOR DATABASE"""

    for index, x in enumerate(range(0, 4)):
        print(f"Item No {index + 1}")
        name = input("Insert author: ")
        placeofBirth = input("Insert place of birth: ")
        # do not add quotes in between column names
        # comma to separate sql and tuple with values
        # format with a tuple and not a list
        cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth) 
        VALUES(?, ?) """, (name, placeofBirth))
        db.commit()


def books():
    """INSERT INTO BOOK DATABASE"""
    for index, x in enumerate(range(0, 12)):
        id = index + 1
        print(f"Item No {id}")
        title = input("Insert Title: ")
        author = input("Insert Author: ")
        datePublished = input("Insert Date Published: ")
        # do not add quotes in between column names
        # comma to separate sql and tuple with values
        # format with a tuple and not a list
        # Don not add column in between the column items when creating a database
        cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished) 
        VALUES(?,?,?,?) """, (id, title, author, datePublished))
        db.commit()


def main():
    print("This is a book database:\n"
          "(1) Add authors\n"
          "(2) Add books")

    userOption = int(input("User Option: "))

    if userOption == 1:
        author()

    elif userOption == 2:
        books()
    else:
        print("wrong input")

main()
