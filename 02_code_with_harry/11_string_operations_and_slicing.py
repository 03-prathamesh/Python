names="Harry,Prathamesh"
print(names[0:5]) #including 0 but not 5
     #this is the slicing of the string  n-1 tak sagle sstring print karel here n is 5
# NOTe->slicing me quate brackets use hote hai aur function me angular brackets

#len() functionn->used to find the length of the string
len1=len(names)
print("Names is a ",len1,"Letter Word")


fruit="MANGO"
sl=fruit[:3]   #python will take automatically 0 instead of that
print(sl)
print(fruit[:]) #python will automaticaly add 0 and length of string ie 5 , so remember this

#negative slicing
frut="GUAVA"
print(frut[0:-3])     # python will automatically give print(frut[0:frut.len()-3])   ie frut[0:2]
print(frut[-3:-1])  # her -3 wwill become len of frut -3 ie 2 and 4 (len(frut)-1)

nm="HARRY"
print(nm[-4:-2])