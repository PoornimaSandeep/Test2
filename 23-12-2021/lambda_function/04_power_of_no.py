print(" Write a python program to generate a function to get the power of a specified number.")

pw=lambda a,b:a**b

a=int(input("enter the number"))
b=int(input("enter the power of that number"))

print("power of specified number is ",pw(a,b))