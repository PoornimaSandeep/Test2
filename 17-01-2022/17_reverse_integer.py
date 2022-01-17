"""
Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.
"""
num=int(input("Enter the input"))
sign=""
s=""
for i in str(num):
    if i=="-":
        sign +=i
    else:
        s +=i

print(sign,s[::-1])
