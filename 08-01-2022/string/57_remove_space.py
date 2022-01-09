"""
remove spaces from a given string
"""
str=input("enter the string with spaces :")
str2=""
for i in str:
    if i==" ":
      continue
    else:
        print(i,end="")

