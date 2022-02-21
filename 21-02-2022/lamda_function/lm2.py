"""
 Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
 also create a lambda function that multiplies argument x with argument y and print the result
"""

v=lambda x:x+15
print("1st program:",v(10))

t=lambda x,y:x*y
print("2st program:",t(10,12))

'''
Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number. 
'''
def fun(n):
    x=lambda x:x*n
    return x
result=fun(10)
print("output of 2:",result(10))

'''
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
'''
lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst=sorted(lst,key=lambda x:x[1])
print("sorted list ",lst)

'''
4.Write a Python program to sort a list of dictionaries using Lambda. 
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

lst=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

lst=sorted(lst,key=lambda x:x['color'])
print("4 sorted lst",lst)

'''
5.Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evn_num=list(filter(lambda x:x%2==0,lst))
print("evn number",evn_num)

odd_num=list(filter(lambda x:x%2 !=0,lst))
print("odd number",odd_num)

'''
6.Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square=list(map(lambda x:x*x,lst))
print('square number',square)

cube=list(map(lambda x:x*x,lst))
print('cube number',cube)

'''
7.Write a Python program to find if a given string starts with a given character using Lambda.
'''
str=lambda x,y:x[0]==y
print(str('apparna','a'))


'''
8.Write a Python program to extract year, month, date and time using Lambda. Go to the editor
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
'''
from datetime import time,date,datetime

date=datetime.now()
print("current date and time",date)

year=lambda x:x.year
print('year',year(date))

month=lambda x:x.month
print('month',month(date))


d=lambda x:x.time()
print('time',d(date))


'9.Write a Python program to check whether a given string is number or not using Lambda'