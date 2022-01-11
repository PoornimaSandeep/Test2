"""
You are given a positive integer . Print a numerical triangle of height  like the one below:

1
22
333
4444
55555
......
"""
size=int(input("Enter the size "))
for i in range(1,size):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")