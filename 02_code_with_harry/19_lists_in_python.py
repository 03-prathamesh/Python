marks=[10,20,30]
print(marks)
print(type(marks))
#how to get the specif element of the list
print(marks[0])
print(marks[1])
print(marks[2])

#print using the for loop
for i in marks:
    print(i)

#list items are seperated by quamas and enclosed within the square brackets


# VERY IMP-> in python in list we can have multile type of datatitems like integer, string ,character in a single list
print("Printing all the elements of the combined list")
combined=[20,30,6,"Prathamesh",True]
for i in combined:
    print(i)


#list item indexing always starts from 0

#lets learn negative indexing

print(combined[-3])
print(combined[len(combined)-3])
print(combined[5-3])
print(combined[2])


#how to check if specific element is in the list or not
if "Prathamesh" in combined:
    print("Yes")
else:
    print("No")


if "am" in "amundkar":   #Output will be "yes"
    print("yes")
else:
    print("No")

    
#Same thing apply for the string also
if "amn" in "amundkar":   #outpt will be "no"
    print("yes")
else:
    print("No")


#how to print all the elements of the list
english_marks=[10,20,30,40]
print(english_marks)
print(english_marks[:])    #these both syntaxes are same

print(english_marks[1:])   #index will be start from 1 till last

print(english_marks[1:-1])   #print(english_marks[1:4])   1 se start hoga aur 4 included nahi hoga
#print(english_marks[:7])   python automaticallly takes 0 there