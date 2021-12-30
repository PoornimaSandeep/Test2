print("Write a Python program to get the date of the last Tuesday")
from datetime import date, timedelta

dt=date.today()

offset = (dt.weekday() - 1) % 7
last_tuesday = dt - timedelta(days=offset)
print("date of the last Tuesday",last_tuesday)