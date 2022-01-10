"""
You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
"""

n=int(input("Enter the number of words"))
l=[]
d={}
for i in range(n):
    word=input("Enter the word ")
    l.append(word)
count=0
for i in l:

    if i not in d:
       count=0
       for j in l:
            if j==i:
               count +=1

    d[i]=count
print(l)
for i in d.values():
    print(i,end=" ,")