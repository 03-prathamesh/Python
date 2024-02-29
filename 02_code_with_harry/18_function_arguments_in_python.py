#TYPE-1
def average(a=4,b=6):            
    print("The average is: ",(a+b)/2)

average()      #bydefault valie a=4 and b=6 will be passed as function argumentss


#TYPE-2
def average2(a=4,b=6):            
    print("The average is: ",(a+b)/2)

average2(1,5)      #now it will take a=1 and b=5 instead of a=4 and b=6



#TYPE-3
def average3(a=9,b=1):            
    print("The average is: ",(a+b)/2)

average3(5)      #now it will take a=5 and b=6(defafult value of b) instead of a=4 and b=6

#type-4 : if i want to give only the value of b
def average4(a=5,b=8):
    print("The average is: ",(a+b)/2)

average4(b=1)       #here value of b will be 1 instead of 8 and a=5 as it is because we havent passed the value of a



#EXAMPLE
def your_name(fname,last_name="Amundkar"):
    print("Your full name is: ",fname," ",last_name)

your_name("Prathamesh")

#type-5 : argument order doesnt matter
def average5(a=5,b=5):
    print("the average is: ",(a+b)/2)

average5(b=3,a=5)