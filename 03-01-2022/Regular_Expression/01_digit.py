import re
print("Sequence Charactres in Regular Expression")
print("1.\d :Represents any digit ")
str='The meeting will be conducted on 1st and 21st of every month'

print()
print("problem 1:create a regular expression to retrieve all words starting with numeric digit")
result=re.findall(r'\d[\w]*',str)  #\d->for digit \w->for alphanumeric *->n number of character
for word in result:
    print(word,end=',')

