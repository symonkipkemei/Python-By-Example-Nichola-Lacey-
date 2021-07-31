'''
121
Create a program that will allow the user to easily manage a list of names. You should
display a menu that will allow them to add a name to the list, change a name in the
list, delete a name from the list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection
to either add a name, change a name, delete a name or view all the names, they
should see the menu again without having to restart the program. The program
should be made as easy to use as possible.
'''

# Display to the user options at hand
# add a name to the list
# change name in the list
# delete name from a list
# view all names in the list
# end the program
# display a suitable message when wrong selection made


nameList = []


def getUserInput():
    print("A program that allows you to manage a list of names\n"
          "(1) Add name to a list.\n"
          "(2) Change name in the list.\n"
          "(3) Delete name from the list.\n"
          "(4) View all names in the list.\n"
          "(5)end program"
          )
    userInput = int(input("Enter one of the options above: "))
    return userInput


# GO GETTER/CONSUMER SUB-PROGRAMS

# add name to a list

def getName():
    addName = input("Insert the name you will like added to the list: ")
    nameList.append(addName)
    return nameList


# change name in the list

def changeName():
    chName = input("Insert name you will like to change: ")
    if chName in nameList:
        index = int(nameList.index(chName))
        nameList.remove(chName)
        newName = input("Insert new name:")
        nameList.insert(index, newName)
    else:
        print("Name not in the list")

def delName():
    delete = input("Insert name you will like to delete")
    nameList.remove(delete)


def viewName():
    for x in nameList:
        print(x)


# THE COMPILER


def main():
    correct = False
    while not correct:
        userInput = getUserInput()
        if userInput == 1:
            getName()
        elif userInput == 2:
            changeName()
        elif userInput == 3:
            delName()
        elif userInput == 4:
            viewName()
        elif userInput == 5:
            correct = True
        else:
            print("You entered a wrong selection")


main()
