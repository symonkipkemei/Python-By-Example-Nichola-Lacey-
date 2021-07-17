'''
087
Ask the user to type in a word and then
display it backwards on separate lines. For
instance, if they type in “Hello” it should
display as shown below:
'''

word = input("Please type in a word: ")
length = len(word)
#slicing to reverse a string
reversedString = word[length::-1]
for x in reversedString:
    print(x)
