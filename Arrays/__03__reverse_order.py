import array as arr
class array3:
    def __init__(self):
        print("Reverse the order of the items in the array.")

    def reverse_ord(self):
        b=arr.array('i',[1,2,3,4,5,6])
        print(b[::-1])

s=array3()
s.reverse_ord()