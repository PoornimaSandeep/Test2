import re
str="hello45665  all how 2333are you "
pattern="all"

match=re.findall(pattern,str)
print(match)

print("")
print("getting letter from str")
pattern2=r'[a-zA-Z]+'
match=re.findall(pattern2,str)
print(match)

print("")
print("getting digit from str")
pattern3= r'[0-9]+'
match=re.findall(pattern3,str)
print(match)

print("")
print("getting both letters and digit")
pattern4=r'[a-zA-z0-9]+'
match=re.findall(pattern4,str)
print(match)

print("")
str2='''
apple
orange
banana
cherries
'''
pattern5=r'.*e'
match=re.findall(pattern5,str2)
print(match)


