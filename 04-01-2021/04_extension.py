"""
 Write a Python program to accept a filename from the user and print the extension of that.
"""
file=input("enter the filename :")
words=file.split('.')
print("file Extension :",words[-1])