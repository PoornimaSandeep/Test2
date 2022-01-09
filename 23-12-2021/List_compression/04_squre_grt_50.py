print("Using list comprehension, construct a list from the squares"
      " of each element in the list, if the square is greater than 50.")
lst1=[2, 4, 6, 8, 10, 12, 14]

lst2=[i*i for i in lst1 if i*i>50]
print(lst2)

