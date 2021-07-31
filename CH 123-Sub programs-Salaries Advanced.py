'''
In Python, it is not technically possible to directly
delete a record from a .csv file. Instead you need
to save the file to a temporary list in Python,
make the changes to the list and then overwrite
the original file with the temporary list.
Change the previous program to allow you to do
this. Your menu should now look like this:
'''

# create a salaries csv
sala = open("salaries.csv", "a")
sala.close()


# SUB PROGRAM B -Go getter ,Get the salaries and name of the user

def getUser():
    name = str(input("Enter your name: "))
    salaries = str(input("Enter your salary: "))
    file = open("salaries.csv", "a")
    newRecord = name + "," + salaries + "\n"
    file.write(newRecord)


def view():
    import csv
    file = open("salaries.csv", "r")
    # converting into an iterable
    reader = csv.reader(file)
    # listing the iterable
    salaList = list(reader)
    for x in salaList:
        print(x)

def deleteRecord():
    import csv
    # open csv and
    file = open("salaries.csv", "r")

    # converting into an iterable
    reader = csv.reader(file)

    # listing the iterable
    salaList = list(reader)

    # create a temporary list
    tmp = []

    # Enumerate row and display each row alongside its index
    # ask user the index of row he/she wants to delete
    # copying list to a temporary list (tmp)

    for index, x in enumerate(salaList):
        print(index,x)
    file.close()
    userRow = int(input("which row do you want to delete?: "))

    #file open csv
    # copy to a list and delete the specified row by the user
    # append the list and overwrite the csv file

    file = open("salaries.csv", "r")
    reader = csv.reader(file)
    salaList = list(reader)
    for x in salaList:
        del x[userRow]
        print(x)

    print(salaList)


def main():
    # ask for user input
    # display menu comes in the main program
    correct = False
    while not correct:
        try:
            print("Salaries Display\n"
                  "(1)Add to a file\n"
                  "(2)View all records\n"
                  "(3)Delete a record\n"
                  "(4)Quit program")
            userInput = (input("Please enter your selection: "))

            if int(userInput) == 1:
                getUser()
            elif int(userInput) == 2:
                view()
            elif int(userInput) == 3:
                deleteRecord()
            elif int(userInput) == 4:
                print("Thank you for participating. The game has ended!")
                correct = True
            else:
                print("You entered a wrong input")
        except ValueError:
            print("You did not enter a number.\n"
                  "You might want to retake your kindergarten classes!\n"
                  "Try again:")

main()
