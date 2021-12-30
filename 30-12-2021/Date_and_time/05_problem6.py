print("Write a Python program to subtract five days from current date.")
from datetime import date,timedelta

dt=date.today()-timedelta(5)
print("Current date",dt.today())
print("5 days before",dt)
print("2 days after",dt.today()+timedelta(2))