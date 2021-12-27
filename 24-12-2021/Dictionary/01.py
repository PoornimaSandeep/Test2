print("create a dictionary from two lists without losing duplicate values.  ")
l1= ["Python", "Java", "Ruby"]

l2 = [78,92,34]
new_dict = {l1[i]: l2[i] for i in range(len(l1))}
print ("Created dictionary:",new_dict)


