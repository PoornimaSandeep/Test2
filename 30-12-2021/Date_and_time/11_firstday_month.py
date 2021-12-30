print("Write a Python program to get the first day of a given month and year.")
import calendar
year = int(input("enter the year"))
month = int(input("enter the month"))
no_of_days=calendar.monthrange(year, month)
print("first day of  this month",no_of_days[0])