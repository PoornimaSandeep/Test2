"""
that accepts a string and calculate the number of digits and letters
"""
str=input("Enter the string :")

digit=[i for i in str if i.isdigit()]
letters=[i for i in str if i.isalpha()]

print("no of digits in string",len(digit))
print(" ")
print("no of letters in string",len(letters))