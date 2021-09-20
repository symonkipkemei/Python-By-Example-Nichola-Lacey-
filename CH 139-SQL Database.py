
# to access sqlite library

import  sqlite3


# when we say connect , we create a database if doesnt exists and named as db
# create an object called cursor
with sqlite3.connect("kiplelgo.db") as db:
    cursor = db.cursor()



# CREATING EMPLOYEES DATABASE

cursor.execute(""" CREATE TABLE IF NOT EXISTS employees(
id integer PRIMARY KEY,
name text NOT NULL,
dep text NOT NULL,
salary integer ); """)

# CREATING MANAGERS DATABASE
cursor.execute(""" CREATE TABLE IF NOT EXISTS departments(
dep text PRIMARY KEY,
manager text NOT NULL) """)

db.commit()

# SAVING INTO A DATABASE

#cursor.execute("""INSERT INTO departments(dep,manager)
#VALUES("sales","rono")""")

# primary key is the unique identifier, the database might have all similar attributes
# but when the primary ky is the same it will not be saved into the database

# ALLOW THE USER TO SAVE TO THE DATABASE FROM INPUT VALUES
# formatting data into the database

newID = input("Enter ID number: ")
newName = input("Enter name: ")
newDept = input("Enter department: ")
newSalary = input("Enter salary: ")

cursor.execute("""INSERT INTO employees(id,name,dep,salary)
VALUES(?,?,?,?)""", (newID, newName, newDept, newSalary))



# DISPLAYING ALL DATA FROM THE DATABASE

cursor.execute("""SELECT * FROM employees""")
print(cursor.fetchall())

# DISPLAYING DATA IN A SINGLE LINE
cursor.execute("""SELECT * FROM employees""")
for x in cursor.fetchall():
    print(x)


# ORDERING DATABASE
print("\ndatabase ordered by name")
cursor.execute("""SELECT * FROM employees ORDER BY name""")
for x in cursor.fetchall():
    print(x)

# DISPLAYING DATABASE AS PER CERTAIN CONDITIONS
print("\nDatabase displaying instances with salaries mire than 20000")

cursor.execute("""SELECT * FROM employees WHERE salary> 20000""")
for x in cursor.fetchall():
    print(x)


# DISPLAYING DATABASE AS PER DEPARTMENT CONDITION
print("\nDatabase displaying employees from architecture department")

cursor.execute("SELECT * FROM employees WHERE dep='architecture' ")
for x in cursor.fetchall():
    print(x)


# DATABASE ONE TO MAY RELATIONSHIP

print("\nDatabase displaying the name of the departments manager")

cursor.execute("""SELECT employees.id, employees.name,departments.manager
 FROM employees,departments WHERE employees.dep=departments.dep
 AND employees.salary > 20000""")
for x in cursor.fetchall():
    print(x)
# NOTE that databases are spelling sensitive and in case you misspell even a single line,
# the database seizes to work

# AlSO NOTE
# the database commands are in capital

# THE USER WITH ULTIMATE POWERS
# ask the user which department he/she would like to display

whichdep = input("Enter a department: ")

cursor.execute("SELECT*  FROM employees WHERE dep=?", [whichdep])
for x in cursor.fetchall():
    print(x)


# RESHUFFLING THE PIG STY (KENYAN CABINET SECRETARIES)
# changing existing data in a databse with new data

cursor.execute("UPDATE employees SET name = 'Toay' WHERE id=28")
db.commit()


# EXECUTING THE PIGS
cursor.execute("DELETE employees WHERE id=41")
db.commit()

# SAVES THE CHANGES TO THE DATABASE AND CLOSES
db.commit()

db.close()
