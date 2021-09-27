
# import sql
import sqlite3
import random

# DISPLAY DATABASE
# Displaying what is in the database
# We are going to fetch what is in the database and display

# connect to the database and create a  cursor object that will allow us to fetch data
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

# Now that we have opened the database, we can go ahead and select everything
# (represented with an asterik)  within the phonebook table.
cursor.execute("SELECT * FROM phonebook")

# display one row after another using loop
for x in cursor.fetchall():
    print(x)




# EXECUTE SOMEBODY FROM DATABASE
# ask for ID from the user
print("we are about to execute you, what's your ID?")
id = int(input("User ID: "))

cursor.execute("DELETE FROM phonebook WHERE ID=?", [id])



# AFTER DELETING

# Now that we have opened the database, we can go ahead and select everything
# (represented with an asterik)  within the phonebook table.
cursor.execute("SELECT * FROM phonebook")

# display one row after another using loop
for x in cursor.fetchall():
    print(x)
