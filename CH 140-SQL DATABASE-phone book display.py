""""
Using the PhoneBook database from program 139,
write a program that will display the following menu.
If the user selects 1, they should be able to view the
entire phonebook. If they select 2, it should allow them
to add a new person to the phonebook. If they select 3, it
should ask them for a surname and then display
only the records of people with the same surname. If
they select 4, it should ask for an ID and then delete that
record from the table. If they select 5, it should end the
program. Finally, it should display a suitable message if
they enter an incorrect selection from the menu.
They should return to the menu after each action, until
they select 5.

"""
# import sql
import sqlite3
import random


def display():
    """We are going to fetch what is in the database and display"""
    with sqlite3.connect("PhoneBook.db") as db:
        cursor = db.cursor()
    # DISPLAY DATABASE
    # Displaying what is in the database
    #
    # Now that we have opened the database, we can go ahead and select everything
    # (represented with an asterik)  within the phonebook table.
    cursor.execute("SELECT * FROM phonebook")

    # display one row after aursor.fetchall():
    for x in cursor.fetchall():
        print(x)
    db.commit()
    db.close()


def addtophonebook():
    """We are going to add user data into the database"""
    with sqlite3.connect("PhoneBook.db") as db:
        cursor = db.cursor()
    # Give the user items to be added in the database
    # Because we already know the number of items to be added, we will use for loop
    # we are going to self generate the user ID using random
    id = random.randint(50, 70)

    for x in range(0, 1):
        firstName = input("Insert First name: ")
        secondName = input("Insert Second name: ")
        phoneNumber = input("Phone Number: ")

        cursor.execute("INSERT INTO phonebook (ID, FirstName, Surname, PhoneNumber) VALUES(?, ?, ?, ?)",
                       (id, firstName, secondName, phoneNumber))

    db.commit()
    db.close()


def search():
    """ Searching for firstname in the database"""
    """We are going to add user data into the database"""
    with sqlite3.connect("PhoneBook.db") as db:
        cursor = db.cursor()

    # SEARCHING FOR SURNAME
    # Searching for items in a database
    # Ask the user what is the name he would like to search for , if it is not there,
    # inform the user the name is not in the database

    searchResult = input("search for the firstName: ")
    cursor.execute("SELECT * FROM phonebook WHERE FirstName = ? ", [searchResult])

    for x in cursor.fetchall():
        print(x)
    db.commit()
    db.close()


def execute():
    """ Searching for firstname in the database"""
    """We are going to add user data into the database"""
    with sqlite3.connect("PhoneBook.db") as db:
        cursor = db.cursor()
    # EXECUTE SOMEBODY FROM DATABASE
    # ask for ID from the user
    print("we are about to execute you, what's your ID?")
    # please note that you first need convert the user entry into an integer , in order for it to work.
    id = int(input("User ID : "))

    cursor.execute("DELETE FROM phonebook WHERE ID=?", [id])
    db.commit()
    db.close()




def main():
    correct = False
    while not correct:
        print(" Select one of the options below\n"
              "1. View phone book\n"
              "2. Add to phonebook\n"
              "3. Search for surname\n"
              "4. Delete person from phone book\n"
              "5. Stop program")

        user = int(input("choose option: "))

        if user == 1:
            display()
        elif user == 2:
            addtophonebook()
        elif user == 3:
            search()
        elif user == 4:
            execute()
        elif user == 5:
            correct = True
        else:
            print("Incorrect value, try again.")

    else:
        print("Great thank you!")


main()