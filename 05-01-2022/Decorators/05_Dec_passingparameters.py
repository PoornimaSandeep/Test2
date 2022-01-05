print("decorator function")

#checking the function for num +ve or -ve
def dec(func):
    def inner(x):
        if x >0:
          return func(x)
        else:
          return f"The given number is negative number ,please give positive number"
    return inner

@dec
def prime_num(x):
    c =0
    for i in range(1,x+10):
        if x%i==0:
            c+=1
    if c==2:
        return f"prime number"
    else:
        return f"not prime number"
    return x

print(prime_num(-1))