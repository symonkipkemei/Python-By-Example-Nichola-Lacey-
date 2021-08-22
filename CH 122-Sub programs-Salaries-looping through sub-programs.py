'''
122
Create the following menu:
If the user selects 1, allow them to add to a file
called Salaries.csv which will store their name
and salary. If they select 2 it should display all
records in the Salaries.csv file. If they select 3 it
should stop the program. If they select an
incorrect option they should see an error
message. They should keep returning to the
menu until they select option 3.
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
    file.close()


def view():
    import csv
    file = open("salaries.csv", "r")
    # converting into an iterable
    reader = csv.reader(file)
    # listing the iterable
    salaList = list(reader)
    for x in salaList:
        print(x)
    file.close()


def main():
    # ask for user input
    # display menu comes in the main program
    correct = False
    while not correct:
        try:
            print("Salaries Display\n"
                  "(1)Add to a file\n"
                  "(2)View all records\n"
                  "(3)Quit program\n")
            userInput = (input("Please enter your selection: "))

            if int(userInput) == 1:
                getUser()
            elif int(userInput) == 2:
                view()
            elif int(userInput) == 3:
                print("Thank you for participating. The game has ended!")
                correct = True
            else:
                print("You entered a wrong input")
        except ValueError:
            print("You did not enter a number.\n"
                  "You might want to retake your kindergarten classes!\n"
                  "Try again:")

main()
