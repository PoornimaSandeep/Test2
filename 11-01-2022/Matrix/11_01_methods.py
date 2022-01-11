print("Methods in an array")
import array as ar

a=ar.array('i',[1,2,3,4,4,5])
print("initial array",a)

a.append(90)
print("after append 90",a)

a.remove(90)
print("after revome an array",a)

a.extend([1,2,33])
print("After extend",a)

print("count of 4",a.count(4))

print("index of element",a.index(5))

