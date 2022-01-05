print("args")
def func(*args):
    for i in args:
        print(i,end=" ")

func(1,2,4,4,2,2)
func("a","b","c","d","e")
