print(" to remove an empty tuple(s) from a list of tuples")

l=[1,2,3,4,2,33,(),45 ]
for i in l:
    if type(i)==tuple:
       l.remove(i)
print(l)