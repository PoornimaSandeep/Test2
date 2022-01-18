'''
Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
'''
l=[i for i in range(1,30)]
print(l)
count=0
for i in l:
    count +=1
    if count==3:
        print(i, end=",")
        count=0
