"""
Sort Counter by value.
"""
from collections import Counter
dict={1: 1, 2: 4, 3: 9,  7: 49, 8: 64,  11: 121, 12: 144, 4: 16, 5: 25, 6: 36,13: 169, 14: 196,9: 81, 10: 100, 15: 225}

d=Counter(dict)

print(d.most_common())