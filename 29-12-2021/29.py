print("You are given  n words. Some words may repeat. For each word, output its number of occurrences. "
      "The output order should correspond with the input order of appearance of the word.")

str =input("Enter the string")
l=str.split()
dict={}

for i in l:
    if i not in dict:
        dict[i]=1
    elif i in dict:
       dict[i] +=1
print("output",dict)