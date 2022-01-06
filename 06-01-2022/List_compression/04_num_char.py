"""
Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
"""
colors=['red','orange','green','yellow','lllllll']

new_list=[len(i) for i in colors ]
print("number of characters in each fruit",new_list)