#calculator program using python
n1=int(input("Enter first Number: "))
n2=int(input("Enter second Number: "))

print("Enter 1 to perform the addition")
print("Enter 2 to perform the substraction")
print("Enter 3 to perform the multilication")
print("Enter 4 to perform the division")

unique=int(input())

if unique==1:
   print(n1+n2)
elif unique==2:
   print(n1-n2)
elif unique==3:
    print(n1*n2)
elif unique==4:
    print(n1/n2)
else:
    print("You entered the wrong input")


