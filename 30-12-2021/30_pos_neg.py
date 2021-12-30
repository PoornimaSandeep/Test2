print("Python Program to Check if a Number is Positive, Negative or 0")

num=int(input("Enter the number"))
srng=str(num)
if srng[0]=='-':
   print(f"{srng} is negative number")
elif srng[0]=='+':
     print(f"{srng} is positive number")
elif srng[0]=='0':
     print(f"{srng} is 0")
else:
    print(f"{srng} positive  number")
