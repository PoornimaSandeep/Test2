"""

Position formula:

Let's assume that the elements of the array are linearly distributed.

General equation of line : y = m*x + c.
y is the value in the array and x is its index.

Now putting value of lo,hi and x in the equation
arr[hi] = m*hi+c ----(1)
arr[lo] = m*lo+c ----(2)
x = m*pos + c     ----(3)

m = (arr[hi] - arr[lo] )/ (hi - lo)

subtracting eqxn (2) from (3)
x - arr[lo] = m * (pos - lo)
lo + (x - arr[lo])/m = pos
pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])


Algorithm
Rest of the Interpolation algorithm is the same except the above partition logic.

Step1: In a loop, calculate the value of “pos” using the probe position formula.
Step2: If it is a match, return the index of the item, and exit.
Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array.
Otherwise calculate the same in the right sub-array.
Step4: Repeat until a match is found or the sub-array reduces to zero.
Below is the implementation of algorithm.
"""


def interpolationSearch(arr, lo, hi, x):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        # Probing the position with keeping
        # uniform distribution in mind.
        pos=lo+((x - arr[lo])*((hi - lo)))//(arr[hi] - arr[lo])

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)

        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1


# Driver code


# Array of items in which
# search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 18, 33, 35, 42, 47]
n = len(arr)

# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n - 1, x)

if index !=  -1:
    print("Element found at index", index)
else:
    print("Element not found")
