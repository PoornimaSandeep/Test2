"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
four of the five integers.Then print the respective minimum and maximum values as a single line of two
space-separated long integers.

"""
l=[1,2,3,4,5]
res=[]
sum=0
for i in range(len(l)-1):
    sum +=l[i]
res.append(sum)
sum=0
for i in range(1,len(l)):
    sum+=l[i]
res.append(sum)

print(res)
