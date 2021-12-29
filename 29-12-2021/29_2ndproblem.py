print("""
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2 to5 , print Not Weird
If  is even and in the inclusive range of  6 to 20 , print Weird
If  is even and greater than 20 , print Not Weird""")
print(" ")
n=int(input("enter the number"))
if n%2 != 0:
    print("Weird")
elif n%2==0 and n in range(2,6):
    print("Not Weird")
elif n%2==0 and n in range(6,21):
    print("Weird")
elif n%2==0 and n >20:
     print("Not Weird")
