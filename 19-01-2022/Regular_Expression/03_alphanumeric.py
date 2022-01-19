print("03.Write a Python program to check that a string contains only a certain set of characters"
      " (in this case a-z, A-Z and 0-9).")
import re
def check_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(check_specific_char("ABCDEFabcdef123450"))
print(check_specific_char("*&%@#!}{"))