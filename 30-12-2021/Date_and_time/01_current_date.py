print("Get Current Date")
from datetime import date,time,datetime

today=date.today()
print("current time now",datetime.now())
print("Current date is :",today)

print("")
print("Get Today’s Year, Month, and Date")
print("Current year",today.year)
print("Current month ",today.month)
print("Current date",today.day)