
list=[1,2,3,34,4,4,4]
print("list printing  ")

try:
    n = int(input("enter the number"))
    print(list[n])
except Exception as e:
    print("exception accours",e)
finally:
    print("we done")

print("thank you")
