print("Integer to roman")

l=[]
prev=0
value=int(input("enter the number"))
#creating list

if value>=1 and value<4:
    print('I'*value)
elif value >=4 and value <9:
    s=value-5
    if s<0:
        print("IV")
    if s>=0:
        print('V'+'I'*s)




