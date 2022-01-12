"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and
last character are same from a given list of strings.
"""
Sample_List =['abc', 'xyz', 'aba', '1221','3445593']
count=0

for i in Sample_List:
     if i[0]==i[-1]:
         count +=1
print("result is",count)
