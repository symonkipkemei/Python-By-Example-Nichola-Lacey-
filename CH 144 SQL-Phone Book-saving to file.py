import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# display all the books
cursor.execute(""" SELECT * FROM Books """)
for x in cursor.fetchall():
    print(x)

# user selected year of publishing
author = input("Author's name: ")

# select all books published with authors name
cursor.execute(""" SELECT * FROM Books WHERE Author=?""", [author])
for z in cursor.fetchall():
    z = list(z)
    file = open("author101.txt", "a")
    record = z[1] + "-" + z[2] + "-" + z[3] + "\n"
    file.write(record)
    file.close()
    print(record)
