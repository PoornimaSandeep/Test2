"""
Implement a function that takes that consists of lowercase letters and digits and
returns string that consists of all digits and lowercase English letters that are not present
in the string.The digits should come first, in ascending order,followed by characters ,also in ascending order
"""
num=['0','1','2','3','4','5','6','7','8','9']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str="34kljkmm6"
res=[]
def missing_char(s):
    ip=[]
    for i in s:
        ip.append(i)
    print(ip)
    for j in num:
        if j not in ip:
            res.append(j)
    for k in alpha:
        if k not in ip:
            res.append(k)
    return "".join(res)

print(missing_char(str))

