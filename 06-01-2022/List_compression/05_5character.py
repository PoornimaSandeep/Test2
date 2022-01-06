"""
make a list that contains each fruit with more than 5 characters
"""

fruits=['Mango', 'Kiwi', 'Strawberry']

new_list=[x for x in fruits if len(x)>4]
print("fruits with more than 5 characters",new_list)