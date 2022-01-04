"""
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
"""

numbers=input("Enter sequence of comma-separated numbers")
li=numbers.split(',')
tu=tuple(li)
print("list :",li )
print("Tuple:",tu)

