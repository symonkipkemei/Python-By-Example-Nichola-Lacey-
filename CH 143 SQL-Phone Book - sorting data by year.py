import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# display all the books
cursor.execute(""" SELECT * FROM Books """)
for x in cursor.fetchall():
    print(x)

# user selected year of publishing
user = int(input("Enter year of publishing: "))

# select all books published after that year
cursor.execute(""" SELECT * FROM Books WHERE DatePublished>=?""", [user])
for z in cursor.fetchall():
    print(z)
# I have no control over the date published because the type
# of stored data is a text and not an integer
