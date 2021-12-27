print("Given a string containing just the characters '(' and ')', "
      "find the length of the longest valid (well-formed) parentheses substring")

"sample string ((()))(("
str=input("enter the paranthesis as a string: ")
#l2=[l[i] for i in range(len(l)) if l[i]=='(']
l=[i for i in str]
l2=[]
count_open=0
count_close=0
value=0
""" here we counting the open and close braces"""
for i in l:
    if i=='(':
       count_open +=1
    elif i==')':
        count_close +=1

"""here we select which one will be less ,then consider that as a value """
if count_open<count_close:
    value=count_open
else:
    value=count_close
""" here we formed the valid  format of paranthesis"""
for i in range(value):
    l2.append("(")
    l2.append(")")

print("The longest valid parentheses substring is:",l2)
print("The length of the srting is :",len(l2))



