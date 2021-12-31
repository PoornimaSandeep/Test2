print("Write a Python program to get the dates 30 days before and after from the current date")
from datetime import date

from datetime import date,timedelta
dt=date.today()
print("Before 30 days: ",dt.today()-timedelta(30))

