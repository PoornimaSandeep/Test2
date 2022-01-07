"""
compute sum of digits of a given string
"""
str=input("Enter the number")

sum=0
for i in str:
    sum +=int(i)
print("sum of digits :",sum)