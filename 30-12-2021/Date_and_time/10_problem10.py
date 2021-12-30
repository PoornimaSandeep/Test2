print("Write a Python program to get the number of days of a given month and year.")
import calendar
year = 2016
month = 6
no_of_days=calendar.monthrange(year, month)
print("no of days in this month",no_of_days[1])