print("1. Write a Python script to display the various Date Time formats:")
"""
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week"""


from datetime import date ,datetime,time
dt=date.today()
print("a) Current date and time :",datetime.now())
print("b) Current year:",dt.year)
print("c) Month of year:",dt.month)
print("d) Week number of the year:",dt.strftime("%W"))
print("e)Weekday of the week:",dt.strftime("%w"))
print("f) Day of year :",dt.strftime("%j"))
print("g) Day of the month :",dt.strftime("%d"))
print("h) Day of week:",dt.strftime("%A"))