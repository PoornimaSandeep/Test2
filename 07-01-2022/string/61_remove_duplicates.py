"""
remove duplicate characters of a given string
"""
str=input("Enter the string :")
s=set(str)
res="".join(s)
print("final string :",res)