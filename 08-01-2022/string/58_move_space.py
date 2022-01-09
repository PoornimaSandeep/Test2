"""
move spaces to the front of a given string
"""
str=input("enter the string with spaces :")
str2=""
for i in str:
    if i==" ":
       print(i,end=" ")
    else:
        str2 +=i

print(str2)
