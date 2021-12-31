def add(n1,n2):
    res=n1+n2
    return res

op_ad=add
op=add(9,12)
print(op_ad) # its printing address of the add function
print(op)
print(op-8)


def mul(n1,n2):
    print(n1*n2)
mul(2,3)
Output=mul(2,3)

def sub(n1,n2):
    return n1-n2   #return is last executable statement if we given any statement after return it should be consider as
                    #dead code
    print("substraction")
s=sub(9,8)
print(s)