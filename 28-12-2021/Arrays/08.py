print("Append items from a specified list.")
import array as arr
l=[1,2,3,45,23,233]
b = arr.array('i', [1, 2, 3, 4, 5, 5,3,6])
b.extend(l)
print(b)