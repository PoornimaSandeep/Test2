"""Check if a given key already exists in a dictionary."""
dict={1:'a',2:'b',3:'5',6:'d'}

k=int(input("Enter key "))
key=["Key is already Exixts"  for x in dict.keys()  if x==k]

if key==[]:
    print("key is not their in this dictionary")
else:
    print(key)
