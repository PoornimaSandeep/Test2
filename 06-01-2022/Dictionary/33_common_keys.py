"""
Match key values in two dictionaries.
"""

d1={1:1,2:2,3:5,4:6}
d2={3:4,4:8,1:4}

for i ,j in set(d1.items()) and set(d2.items()):
    print("comman key values",i,j)