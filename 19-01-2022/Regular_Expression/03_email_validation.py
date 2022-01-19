import re

email='''
poornima@gmail.com
90uyrur884@gmail.com
jfkfjj.com
ikfhifhfh
'''

pattern=r'[a-z0-9]+[0-9]*[a-z]*@[a-z]+\.com'

match=re.findall(pattern,email)
print(match)