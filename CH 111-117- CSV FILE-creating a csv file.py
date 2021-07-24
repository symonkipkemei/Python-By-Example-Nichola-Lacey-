'''


Create a .csv file that will store the following data. Call it “Books.csv”.
'''


import  csv

dataset = open("Books.csv", "w")
for index, x in enumerate(range(1, 6)):
    print("Book no", index)
    title = input("Input title of book: ")
    author = input("Input name of the author: ")
    year = input("Input year of publishing: ")
    info = title + "," + author + "," + year + "\n"
    dataset.write(str(info))
dataset.close()
