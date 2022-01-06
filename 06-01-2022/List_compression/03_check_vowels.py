"""
Use a list comprehension to make a variable named colors_with_two_or_more_vowels.(ex 2: colors with 2 vowels)
Hint: You'll need a way to check if something is a vowel.
"""
from collections import Counter
import re
colors=['red','orange','green','yellow','lllllll']
vowels=['a','e','i','o','u']
colors_with_two_more_vowels = [i for i in colors if len(re.sub(r"[^aeiouAEIOU]", "", i)) > 2]

print("color have more than 2 vowels" ,colors_with_two_more_vowels)

