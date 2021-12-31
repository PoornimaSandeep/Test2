print("nested function ")

def math(n1,n2):
    print("all arithmatic operations")
    def add():
        print("addition")
        res=n1+n2
        return res
    def sub():
        print("substraction")
        res=n1-n2
        return res
    if n1 <n2:
       return add()
    else:
        return sub()

op=math(30,4)
print(op)


