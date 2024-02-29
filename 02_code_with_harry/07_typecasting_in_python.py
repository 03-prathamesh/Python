a="1"
b="2"

print(a+b)     #it will give 12 because their is string concatenation

ab="Prathamesh"
ba="bhawa"
print(ab+ba)


#Explicit typecasting
num1="1"
num2="2"
print(int(num1)+int(num2)) #this is the syntax for the typecating

num3=("harry")
#print(int(num3))   #here python interpreter will give you error because we cannot convert the string to integer
#if there were a string number then we would have converted it to integer. so remember this


#Implicit type casting
c=1.9
d=8    #python will convert this integer to float as 8.0
print(c+d)

e=2.0
print(type(e))
