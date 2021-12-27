print("methods in the list")

s={1,2,34,23,12,11}
print("	1.Adds an element to the set")
s.add(100)

print("")
print("2.copy the set")
x=s.copy()
print(x)

print("")
l={90,89,949}
print("3.clear the set")
l.clear()
print(l)

h={2,34,23,322,3,3333}
print("")
print("4.difference of the set")
k=x-h
print(k)

print("")
print("5.intersection ")
k=x.intersection(h)
print(k)

print(" ")
print("6.union")
k=x.union(h)
print(k)

y = {23,34}
print(" ")
print("7.issuperet")
z = x.issuperset(y)
print(z)
