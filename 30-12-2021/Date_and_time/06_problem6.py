print("7. Write a Python program to print yesterday, today, tomorrow.")
from datetime import date,timedelta
dt=date.today()
print("Yesterday: ",dt.today()-timedelta(1))
print("Today: ",dt)
print("Tomarrow: ",dt.today()+timedelta(1))
