
from itertools import permutations,combinations

n=int(input("enter the number"))
open='{'
close='}'
s='{}'
l=[]
l2=[]
str2=''
str1=''

for i in range(n):

    #l.append(close)
    if i>0:
        l.insert(i,s)

    else:
        l.append(open)
        l.append(close)
#print(str1)
for i in range(n):
    l2.append(open)
for i in l:
    str1 +=i
for i in l2:
    str2 +=i
for i in range(n):
    str2 +=close


print(str1)
print(str2)


