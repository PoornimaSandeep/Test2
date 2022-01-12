"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.
"""
arr=[-4 ,3 ,-9, 0 ,4, 1]
l=len(arr)
res=[]
for i in arr:
    k=i/l
    q = "{:.6f}".format(k)
    if k>0:
       res.append(q)

for i in res:
   print(i)