name="Prathamesh"   #this is a string which is under double quotes
friend="july"
anotherFriend='Priti'    #string can be enclosed within single quotes also  

print("Hello, "+name)
print("hello,",name)   #this will add the one space(, will add)
print("He said \"I am the best\"")
#alternative of this is
print('He said"I am the Best"')

#this is the new syntax in python which is not in cpp
apple='''He said,
"This is my world"
 And i am living in this world
'''
print(apple)


nam="Prathamesh"
# print(nam[0])
# print(nam[1])  you can use for loop instead of that for traversing
# print(nam[2])
# print(nam[3])
# print(nam[4])
# print(nam[5])
# print(nam[6])
# print(nam[7])
# print(nam[8])
# print(nam[9])

#print(nam[10]) it will give the error because their is no index 10 in the nam string
print("Lets use a \"FOR LOOP\"")
for i in nam:
    print(i,end='')   # thi is the main use of end , all characters one by one on a single line, 
    #bydefault python interpreter will print the every character on the new line