"""
You will be given an array of integers. All of the integers except one occur twice.
That one is unique in the array. Given an array of integers, find and print the unique element.
"""
def lonely_integer(a):
    res = 0
    for elem in a:
        res ^= elem
    return res


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))