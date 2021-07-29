# Sub programs
# These are blocks of code that enable us to break programmes into small chance\
# it makes it easier to deal with repetitive tasks like

# Welcoming your user
# Asking the user to input his/her name

def welcome():
    print("Welcome to my programme !")


welcome()

# The first programme ask for the user name
def userName():
    user = input("Please enter your name: ")
    return user

# the second sub program, depends on the argument to display message
# the user within the brackets acts as a holder position
def welcome(user):
    print("welcome", user, "Keep working hard do not give up")

# this is the main programme
# it derives the variable form the first programme
# and stores it in a variable
# the variable is then declared as an argument to the second programme for it to run

def main():
    kipchumba = userName()
    welcome(kipchumba)


main()


# the return key allows data to be retrieved by one programme and used by another.
