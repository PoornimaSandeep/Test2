print("Given an array nums of distinct integers, return all the possible permutations.")
from itertools import permutations
import array as arr

array_list=arr.array('i',[1,2,3])

def perm(arr):
    l = permutations(array_list)
    for i in l:
        print(i,end=", ")
perm(array_list)




