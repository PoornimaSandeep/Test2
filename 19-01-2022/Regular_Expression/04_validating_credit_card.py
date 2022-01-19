"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not.
You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4,5 ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
"""
import re


def isvalid(s):
    value=re.compile(r'[4,5][0-9][-]*')
    return value.match(s)

isvalid("844983893848949")

if isvalid("4498-3893-8489-49"):
    print("valid")
else:
    print("invalid")