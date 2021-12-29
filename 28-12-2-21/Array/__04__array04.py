print("Remove the first occurrence of a specified element from an array.")
import array as arr
b = arr.array('i', [1, 2, 3, 4, 5, 5,3,6])
b.remove(3)
print(b)