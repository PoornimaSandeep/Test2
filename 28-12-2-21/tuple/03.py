print("count the elements in a list until an element is a tuple")

l=[1,2,3,4,2,33,(2,3,4,4222),45 ]
c=0

for i in l:
     if type(i)==tuple:
         break;
     else:
         c += 1
print("count",c)
