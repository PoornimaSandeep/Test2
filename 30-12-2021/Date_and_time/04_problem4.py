print("Write a Python program to determine whether a given year is a leap year.")

yr=int(input("enter the year"))

if yr%4==0:
    print(f"{yr} this is leap year")
else:
    print(f"{yr} this is not  leap year")