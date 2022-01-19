"""start with"""
import re

phone_no='7890989999'



def isvalid(s):
    value = re.compile(r'[6-9][0-9]{9}$')
    return value.match(s)

if isvalid(phone_no):
   print("valid mobile number")
else:
    print("invalid mobile number")