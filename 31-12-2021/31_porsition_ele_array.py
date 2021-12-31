print("""Given an array of integers nums sorted in non-decreasing order, find the starting and 
ending position of a given target value.If target is not found in the array, return [-1, -1].""")

import array as ar

a = ar.array('i', [1, 2, 3, 4, 5,5,6,7,4,3,5,6,44,44,4])
b=sorted(a)
print(b)
search=int(input("Enter the element you want search"))
for i in range(len(b)):
    if b[i]==search:
        print(i,end=" ")


