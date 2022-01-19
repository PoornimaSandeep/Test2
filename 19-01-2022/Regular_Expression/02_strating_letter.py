import re
print("2.\w Represents alphanumeric")
print("Problem2:Create a RE to retrieve all words starting with given string")
str2="an apple away a day keeps the doctor away"
res=re.findall(r'a[\w]*',str2)
for i in res:
    print(i,end=' ')
