
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()


# display all the authors
cursor.execute(""" SELECT * FROM Authors """)
for x in cursor.fetchall():
    print(x)


# user place of birth

user = input("Enter place of Birth: ")

# show books as per user location

# note that when querying data from particular condition, we use list and not tuple
cursor.execute(""" SELECT Books.Title,Books.DatePublished,Books.Author FROM Books,Authors
 WHERE Authors.PlaceofBirth =? AND Books.Author = Authors.Name """, [user])
for y in cursor.fetchall():
    print(y)

