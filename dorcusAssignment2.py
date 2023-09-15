
studentsMarks = [70,80,90,75]
print(studentsMarks)

# Replacing a value 
studentsMarks[2] = 89
print(studentsMarks)

#append item 55
studentsMarks.append(55)
print(studentsMarks)

#size of the list having appended item 55
print(len(studentsMarks))

#program to sum all items in the list
total = sum(studentsMarks)
print(total)

#function that takes two lists and returns true, if they have atleast one common member
list_one= input("enter members")
list_two= input("enter members")
common_member= 5
if 5 in list_one and list_two:
     print("true")