"""
Replace dictionary values with their sum.
"""

dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


for i,j in dict.items():
    ele=str(j)
    sum=0
    for k in ele:
        sum +=int(k)
    dict[i]=sum
print(dict)