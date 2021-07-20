'''
100
Create the following using a 2D dictionary showing
the sales each person has made in the different
geographical regions:

'''

# use a dictionary to store this set of data


# create dictionaries to store data sets for each person and their places

john = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
Tom = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
Anne = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
Fiona = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}

salesDataSet = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
                "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
                "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
                "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

print(salesDataSet)

userName = input("Input your name: ")
userRegion = input("Input your region: ")

print(salesDataSet[userName][userRegion])

# Change data
userNameChange = input("Input the name you want to change: ")
userRegionChange = input("Input the region you want to change: ")
changeData = int(input("Input the new data: "))

salesDataSet[userNameChange][userRegionChange] = changeData

for y in salesDataSet:
    print(salesDataSet[y][userRegionChange])


