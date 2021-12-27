print("Create a list of all the consonants in the string "
      "“Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”")

vowels=['a','e','i','o','u']
str="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
str2=str.lower()

lst=[i for i in str2 if i not in vowels if i !=' ']
s=set(lst)
print(list(s))