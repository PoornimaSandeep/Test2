"""
find mediain value
"""
import statistics

def median(arr):
    a=statistics.median(arr)
    return a

arr=[1,2,3,45,5]
print(median(arr))