''' 1.Write a lambda function that takes x as parameter and returns x+2. Then assign it to a variable named L.'''

l=lambda x:x+2
print(l(10))


'''
2. Write a lambda function which takes z as a parameter and returns z*11
Assign it to variable named: f.
'''
f=lambda x:x*11
print(f(10))


'''
3.Write a function which takes two arguments: a and b and returns the multiplication of them: a*b. 
Assign it to a variable named: f.
'''
f=lambda x,y:x+y;
print(f(8,9))

'''
4.Using .sort() method, create a lambda function that sorts the list in descending order. 
Refrain from using the reverse parameter.
'''
lst=[100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x:100/x)
print(lst)


'''
5.This time use the sorted() function to sort the list in ascending order with lambda.
'''
lst=[100, 10, 10000, 1, 9, 999, 99]
ls=sorted(lst,key=lambda x:100/x,reverse=True)

print(ls)

'''6.Using sorted() function and lambda sort the words in the list based on their second letter from a to z.'''
lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
lst=sorted(lst,key=lambda x:x[1])
print(lst)

'''7.Using sorted() function and lambda sort the tuples in the list based on the second items.'''
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst=sorted(lst,key=lambda x:x[1])
print(lst)


'''
8.Using sorted() function and lambda sort the tuples in the list based on the last character of the second items.
'''
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

lst=sorted(lst,key=lambda x:x[1][-1])
print(lst)


'''
9.Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the 
last character of the second items in reverse order.
'''
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst=sorted(lst,key=lambda x:x[1][-1], reverse=True)
print(lst)

'''
'''