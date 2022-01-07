"""
Reverse each word in given string Input
"""
str=input("Enter the input: ")
words=str.split()

for i in words:
    print("Reverse string : ",i[::-1],end= " ")