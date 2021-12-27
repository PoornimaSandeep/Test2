print("Write a recursive function that takes an array that may contain more arrays "
      "in it and returns an array with all values flattened.")
l=[3,[1,2,3],[5,6],[7,8,9]]

def flatten_list(l):
    if len(l)==0:
       return []
    if type(l[0]) is not list:
        return [l[0]]+flatten_list(l[1:])
    else:
         return[i for i in l[0]]+flatten_list(l[1:])

def flatten(l):
    res=[]
    if len(l)==0:
        return []
    if type(l[0] is list):
       return res.extend(flatten(l[0]))+flatten(l[1:])


a=flatten_list(l)
print(a)