print("Write a recursive function that takes an list and a callback function and returns True "
      "if any value of that list returns True from that callback function otherwise returns False.")
l=[1,3,5,9]

def even_num(l):
    if len(l)==0:
        return False
    elif l[0]%2==0:
        return True
    return even_num(l[1:])

e=even_num(l)
print(e)
