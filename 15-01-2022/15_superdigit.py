"""
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2
"""


def superdigit(num):
    st=str(num)
    sum =0
    for i in st:
        sum +=int(i)
    if sum>9:
        return superdigit(sum)
    else:
        return sum
#9875987598759875
a=superdigit(9875)
print(a)

