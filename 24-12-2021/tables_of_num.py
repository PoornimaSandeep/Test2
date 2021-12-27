print("Display Multiplication Table for the given number.")
num=int(input("enter the num"))

for i in range(1,11):
    res=num*i
    print(f"{num}*{i}={res}")
