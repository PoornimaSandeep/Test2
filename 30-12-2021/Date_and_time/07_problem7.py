print("Write a Python program to get the current week")
from datetime import date
dt=date.today()
print("current week ",dt.strftime("%A"))