
for index, x in enumerate(range(0, 4)):
    # lets first open the csv file
    file = open("Books0.csv", "a")

    print("This file is no", index + 1)
    Book = input("insert book name:")
    Author = input("insert author name:")
    YearReleased = input("insert year realised:")

    # create a line of information
    record = Book + "," + Author + "," + YearReleased + "\n"
    file.write(record)
    file.close()



