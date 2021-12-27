print("Write a recursive function that takes a string and reverse the string.")
l=['kanak','nayan','mamatha','pallavi']

def rev_str(l):
    if len(l)==0:
        return []
    else:
        str=''
        for i in l[0]:
             str +=i
        return [str[::-1]]+rev_str(l[1:])
a=rev_str(l)
print(a)