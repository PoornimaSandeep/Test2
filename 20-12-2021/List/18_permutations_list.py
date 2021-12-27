print("All permutations of list elements")
from itertools import permutations

# Get all permutations of [1, 2, 3]
l=[3,4,5]
perm = permutations(l,3)

# Print the obtained permutations
for i in list(perm):
    print(i)