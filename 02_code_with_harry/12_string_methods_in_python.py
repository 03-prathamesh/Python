# 1]LEN()
name="Pratamesh"
print(len(name))
#strings are immutable in python
name="PATthy"       
print(name)

print(name.upper())   #converts our string into the uppercase
print(name.lower())   #converts our string into the lowercase

# 2]RSTRIP() method is used to remove the trailing characters from the string
#trailing means after the character
nm="Harry!!!!!"
print(nm.rstrip("!"))
print(len(nm))


# 3]REPLACE() method->used to split a string into the list of substrings
nmm="CARRY"
print(nmm.replace("C","J"))      #sare ke sare c j me change ho jayenge
print(nmm.replace("C","Jo"))
print(nmm)     #it will print the original string , that is you cant modify the string, because strings are immutable but you can change the value of string as i did in line no.4....


# 4]SPLIT() method
p="Prath amesh"
print(p.split(" "))     #it is used to convert a string to list


date = "2023-09-21"
st=date.split('3')
s=date.split('-')

print(st)
print(s)


# 5] CAPITALIZE() method
blogHeading = "introduction to python"    #is pure string ka pehla character capitalise ho jayega
print(blogHeading.capitalize())

#it also correct the error like jS   it will correct to js,ie only first char is uppercase and all othe in lowercase
blogHeading2="introduction To jS"
print(blogHeading2.capitalize())

# 6]CENTRE() method->align the string to the centre as the parameter given
str1="Welcome to the console!!!"
print(str1.center(50))    #yat 25 spaces add hotat , karan 25 len aahe str1 chi so 25+25=50
print(len(str1))
print(len(str1.center(50)))


# 7] COUNT() -> return number of times the given value has occured

ap="My name is prathamesh and there is alot to do now"
n=ap.count("is")
print(n)

# 8]ENDSWITH() ->Checks if the string end with the given value or not
str2="Welcome to the college!!!"
print(str2.endswith("!!!"))

str3="Welcome to the college"
print(str3.endswith("e"))
print(str3.endswith("to",4,10))   #come to hi string tr 2 ne end hote

str3="Welcome to the college"   #in python , you can override a variable -------->note this

# 9] FIND() method-> search for the first occurence of the given value and returns the index where it is present
# is the given value is absent from the string then return -1

str3="He's name is Prathamesh and he is a smart boy"
print("The index of \"is\" is :",str3.find("is"))   #return index of i ie 10
print(str3.find("Z"))   #return -1 necause this type of character is not present in the strin



# 10]INDEX() method -> same as find() function but raises an exception if the value is absent whereass find does not
# print(str3.index("z"))      it will give a error or exception

# 11] ISALNUM() -> it returns true only if entire string only consist of A-Z, a-z , 0-9, 
#if any other character or punctuation are present then it returns false

tr="Prathamesh"
print(tr.isalnum())


tr1="Prathamesh,"
print(tr1.isalnum())

#check for space also
tr4="Prathamesh is good boy"
print(tr4.isalnum())      #is will also nnot count space and return false for space.


#12] isalpha() - same as ISALNUM but difference is 0-9 numbers  shoulf be not there only A-Z and a-z
tr3="Hrry3"
print(tr3.isalnum())
print(tr3.isalpha())


# 13]ISLOWER()-> it will check is all characters are in lowercase or not
l1="Harr"
print("All characters are in lowercase is:",l1.islower())


# 14] ISPRINTABLE() -> returns true if all the values within the given strings are printable, if not then returns false
# means return false is string has any termination characaters lile \n \t  ""
check="hello prathame\nsh"
check2="hello prathamesh\n"   # it will directly give the new line to us

print(check.isprintable())
# print(check)

# 15] ISSPACE() ->returns true only and only if the string containt white spaces else returns false

ch="   "
ch1="prathamesh  is  a male"
print(ch1.isspace())


# 16]ISTITLE() -> returns true only if the  first letter of each word of the string is capitalised
s1="World health organization"
print(s1.istitle())

# 17]title() -> convert first character of each string to the uppercase
s2="world health organization"
print(s2.title())

# 18]isUpper->returns true if all the characters in the string are uppercase
temp="PRATHEMESH"
print(temp.isupper())


# 19]startsWith()-> used to check if the string starts with a given value or not
str11="Python is interpreted langauage"
print(str11.startswith("P"))
print(str11.startswith("p"))      #for ssmall p it wil give false
print(str11.startswith("Python"))      #true


# 20]swapcase()->  changes the character casing of the string , ie upper ko lower and lower ko upper

u1="THis is The python Tutorial"
print(u1.swapcase())


