print("Write a Python program to create a HTML calendar with data for a specific year and month.")
import calendar
htmlcal=calendar.HTMLCalendar(calendar.MONDAY)
print(htmlcal.formatmonth(2022,1))