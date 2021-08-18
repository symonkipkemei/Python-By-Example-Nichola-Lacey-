# you need to first import csvfor it to work


file = open("Graduation.csv", "w")

record = "symon" + "," + "A" + "," + "98" + "," + "Excellent work" + "\n"
file.write(str(record))

# it is good practice that you first convert the record into a string
# before writing it into a csv file
file.close()



#when you wat to add files without deleting,
# we will use the append command

file = open("Graduation.csv", "a")
name = input("Insert your name:")
grade = input("Insert your grade:")
name = input("Insert your marks")
comments = input("Insert comments:")

newRecord = name + "," + grade + "," + name + "," + comments + "\n"
file.write(str(newRecord))
file.close()



# did not  do much today.I will try again tomorrow