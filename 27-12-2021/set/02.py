print("Write a Python program to remove the intersection of a 2nd set from the 1st set")

s1={12,3,112}
s2={12,3,232,22,112,89}

s3=s2.intersection(s1)
print(s2-s3)