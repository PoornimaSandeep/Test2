"""Write a Python function that takes two lists and returns True if they have at least one common member."""

def common_ele(l1,l2):
    for i in l1:
        for j in l2:
            if j==i:
                return True
            else:
                return False
l1=[1,2,3,4]
l2=[56,6]
print(common_ele(l1,l2))