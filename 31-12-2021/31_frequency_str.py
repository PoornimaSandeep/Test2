print("Given a string s, sort it in decreasing order based on the frequency of the characters. "
      "The frequency of a character is the number of times it appears in the string.")
str=input("enter the string")
d={}

for i in str:
    if i not in d:
        d[i]=1
    elif i in d:
        d[i] +=1

res=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

print(res)

for i ,j in res.items():
    print(i*j,end=" ")



