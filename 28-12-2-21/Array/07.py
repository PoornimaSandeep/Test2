print("Insert a new item before the second element in an existing array.")
import array as arr
b = arr.array('i', [1, 2, 3, 4, 5, 5,3,6])
b.insert(1,90)
print(b)