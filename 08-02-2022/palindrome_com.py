from itertools import combinations,permutations
n=int(input("enter the number"))
num = str(n)
l=[]
if n>9:
   for i in num:
       l.append(i)

def palind(n):
    rs=[]
    for i in n:
        j=i[::-1]
        if j==i:
           if i not in rs:
              rs.append(i)
    if len(rs)>=1:
       print(max(rs))
    else:
       print(-1)



res=permutations(l)
data=[]
for i in res:
    op="".join(i)
    data.append(op)

palind(data)
