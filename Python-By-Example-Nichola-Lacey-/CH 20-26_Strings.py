'''
020
Ask the user to enter
their first name and
then display the
length of their name.
'''


userName = input("Enter your name: ")
print(len(userName))


'''
021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
'''

#username and surname
firstName = input("Enter you first name: ")
secondName = input("Enter you second name: ")
#joining
joinedName = firstName + " " + secondName
#print name and length
print(joinedName)
print(len(joinedName))

'''
022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result
'''

#username and surname
firstNameA = input("Enter you first name in lower case: ")
secondNameA = input("Enter you second name in lower case: ")

#change names to title case
firstNameA = str.capitalize(firstNameA)
secondNameA = str.capitalize(secondNameA)

#join
joinedNameA = firstNameA + secondNameA

#print
print(joinedNameA)

'''
023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
'''

# Ask and input user rhyme
userRhyme = input("Please enter the rhyme you used to sing in nursery school: ")
# Display length of rhyme
print(len(userRhyme))
# Ask for starting and ending number
startNum = int(input("Please enter a starting number: "))
endNum = int(input("Please enter a ending number: "))
# Display the section of text from start to end number
print(userRhyme[startNum: endNum])

'''
024
Ask the user to type in any word and display it in
upper case.
'''
# Ask user for any word
userWord = input("Please type any word: ")

# change string to uppercase
userWord = str.upper(userWord)

# Display string
print(userWord)


'''
025
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.
'''

# Ask user Firstname
userFirstname = input("Please input your firstname: ")


# check length of user Firstname
lenUserFirstname = len(userFirstname)

# check under five length condition
# If condition is true ask them to enter Surname
# concatenate first and surname without space
# display joined name in uppercase
if lenUserFirstname < 5:
    userSecondName = input("Please input your second name: ")
    joinedNameB = userFirstname + userSecondName
    joinedNameB = str.upper(joinedNameB)
    print(joinedNameB)
# if condition is false display first name in lowercase
else:
    print(str.lower(userFirstname))


'''
026
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.
'''

# Ask user for a word
userWord = input("Please insert a word: ")
userWord = str.lower(userWord)
# create first letter variable
firstLetter = userWord[0]
print(firstLetter)


# if true, concatenate userWord with the string "way"
# display in lower case

'''logical operators separates different conditions'''

if firstLetter == "a" or firstLetter == "e" or firstLetter == "i" or firstLetter == "0" or firstLetter == "u":
    joinedVowelWord = userWord + "way"
    print(joinedVowelWord)
# If condition is false, concatenate userWord, first letter and string "ay"
# Establish length of user word
# display from index to length + one
# display in lowercase
# check if first letter is a vowel
else:
    joinedConsonantWord = userWord + firstLetter + "ay"
    lenOfUserWord = len(joinedConsonantWord)
    print(joinedConsonantWord[1:lenOfUserWord])























