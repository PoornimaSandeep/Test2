print(" Write a python program to generate a lambda function"
      " to separate the odd and even number from a list of numbers")

l=[1,2,4,45,34,234,123456,32342,11233]

even = list(filter(lambda a: (a%2 == 0) ,l))
odd = list(filter(lambda a: (a%2 != 0) ,l))
print("even lsit ",even)
print("odd list",odd)
