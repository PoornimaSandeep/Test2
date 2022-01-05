"""
decorators: Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
            without permanently modifying it
            A function is an instance of the Object type.
            You can store the function in a variable.
            You can pass the function as a parameter to another function.
            You can return the function from a function.
            You can store them in data structures such as hash tables, lists, …

The main objective of decorator functions is we can extend the functionality of existing
functions without modifies that function.


"""
print("1,Treating the functions as objects. ")

def greeting(txt):
    return txt.upper()

print(greeting("hello"))

print("2: Passing the function as an argument ")

def welcome(func):
    res=func("hello every one")
    return res

print(welcome(greeting))

print(" 3: Returning functions from another function.")
def math(x):
    def add(y):
        return x+y
    return add
op=math(80)
print(op(60))


