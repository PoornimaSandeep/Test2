"""Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)"""

n=int(input("enter the n value"))

dict={x:x*x for x in range(1,n)}
print("the dictionary is",dict)