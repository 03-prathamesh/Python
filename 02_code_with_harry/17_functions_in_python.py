def isGreater(a,b):
    if a>b:
        print("first Number",a,"is Greater")
    else:
        print("Second Number",b," is Greater")

a=13
b=20
num1=100
num2=90
isGreater(a,b)
isGreater(num1,num2)


#return type int function in python
def isSmaller(a,b):     #here a and b are required arguments
    if a<b:
        return a
    else:
        return b

n1=100
n2=300
print("The smallest number is:",isSmaller(n1,n2))