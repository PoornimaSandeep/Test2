import array as arr
print("Convert an array to an ordinary list with the same items.")
b = arr.array('i', [1, 2, 3, 4, 5, 6])
c=list(b)
print("type of list",type(c), "the list is ",c)