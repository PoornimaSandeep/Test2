"""Sum all the items in a dictionary"""
dict={i:i*i for i in range(10)}
item=sum(x for x in dict.values() )

print("Dictionary :",dict)
print("sum of all items :",item)