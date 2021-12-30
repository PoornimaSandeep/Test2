from datetime import date,datetime,time

dte=date(2021,12,23)
tm=datetime.now()
print("time :",tm)
print("date :",dte)
print(dte.strftime("%a,%A,%w,%d,%b,%B,%m,%y,%Y"))
print(tm.strftime("%H,%I,%p,%M,%S,%f,%Z"))
