"""
You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa.
"""

str=input("enter the string :")

for i in str:
    if i.isupper():
        print(i.lower(),end="")
    if i.islower():
        print(i.upper(),end="")