# How do you edit an existing csv files by coping to a temporary list

# lets first create our own problem
# a csv file that contains
# the name, the  4 digit id and the amount of contribution each month
# we are going to store this information
# and then edit the ID of one of the users

# a sub program that collects data information( Go getter0


def getInfo():
    name = input("Enter your surname: ")
    ID = input("Insert you ID no-4 digit: ")
    income = input("Insert your net income this month:")
    info = (name, ID, income)
    return info


# a consumer sub programme that picks the values and stores in a csv file
def savecsv(name, ID, income):
    file = open("formode.csv", "a")
    # when retrieving data stored in a tuple, you call the sub programme and not the tuple variable.
    # for instance as shown in the line of code below
    record = str(name) + "," + str(ID) + "," + str(income) + "\n"
    file.write(record)
    file.close()


# a sub programme that opens csv file and reads it
def reader():
    import csv
    file = open("formode.csv", "r")
    read = csv.reader(file)
    read = list(read)
    for x in read:
        print(x)


# A sub program thet enumerates all the available data and sak user which row he/she wants to delete
# we will use insert and remove functions to remove an entire row and replace with a new one within the same position
# this is a masterstroke!

def choose():
    # enumeration of all rows in the csv
    import csv
    file = open("formode.csv", "r")
    read = csv.reader(file)
    read = list(read)
    for index, x in enumerate(read):
        print(index, x)

    # creation of empty list to store our data temporarily
    tmp = []
    for x in read:
        tmp.append(x)
    file.close()

    # ask user which row he/she would like to edit

    editRow = int(input("From above index, which index row would you like to edit? "))

    # ask user which column he would like to change
    change = input("Which of the following would you like to change surname(s) or ID number(i) or Contributions(c)?: ")
    change = change.lower()
    if change == "s":
        NewSurname = input("enter the new surname: ")
        newRecord = str(NewSurname) + "," + str(read[editRow][1]) + "," + str(read[editRow][2]) + "\n"
        del tmp[editRow]
        tmp.insert(editRow, newRecord)

    elif change == "i":
        NewID = input("enter the new ID: ")
        newRecord = str(read[editRow][0]) + "," + str(NewID) + "," + str(read[editRow][2]) + "\n"
        del tmp[editRow]
        tmp.insert(editRow, newRecord)

    elif change == "c":
        NewSalary = input("enter the new contribution: ")
        newRecord = str(read[editRow][0]) + "," + str(read[editRow][1]) + "," + str(NewSalary) + "\n"
        tmp.insert(editRow, newRecord)

    else:
        print("You entered a wrong input")

    # Overwriting the existing csv with new information
    file = open("formode.csv", "w")
    # a csv file only accepts string as an argument and not list
    # convert list to a string
    for row in tmp:
        record = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "\n"
        file.write(record)
    file.close()


# write the main code which is the compiler
def main():
    # project description
    print("This is formode database (csv format) \n"
          "featuring the contributions of each member\n"
          "choose one option from the menu below.")
    correct = False
    while not correct:
        print("(1)Input a new csv\n"
              "(2)Edit existing information\n"
              "(3)Display the database\n"
              "(4)Quit programme")
        userOption = int(input("Choose one option: "))

        if userOption == 1:
            name, ID, income = getInfo()
            savecsv(name, ID, income)
            correct = False

        elif userOption == 2:
            choose()
            correct = False

        elif userOption == 3:
            reader()
            correct = False

        elif userOption == 4:
            correct = True

        else:
            print("You entered a wrong option")
            correct = False


# sub programs are independent pieces of code that depend on one another.
# in most instances they communicate in the main programme where exchange of information happens.
main()

# What if I want to change a value I inserted mistakenly
# How do I go about it?
