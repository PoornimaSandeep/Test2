"""
Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
"""
print("1.accepts fullname and reverse into lastname and firstname")
name=input("Enter the your Full name")
words=name.split()
print(str(words[-1]),words[0])

First_name=input("Enter your first name")
Last_name=input("Enter your Last name")
print("hello "+Last_name+" "+First_name)

