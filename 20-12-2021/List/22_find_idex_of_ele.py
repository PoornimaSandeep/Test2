print("Finding index of an item in specified list")
l=[45,6,78,89,809,8576]

ch=input("which element you want to find the index")

try:
    print(f"index of {ch} is :", l.index(int(ch)))
except Exception as e:
    print("error is: ",e)



