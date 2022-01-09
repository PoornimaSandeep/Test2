from itertools import combinations
print("print a string using this keypad")
print("""
      2:abc 3:def 4:ghi
      5:jkl 6:mno 7:pqrs
      8:tuv 9:wxyz 

""")
d={2:["a","b","c"],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

n=int(input("enter how many character you want to print"))
l=[]
str=""
for i in range(n):
    key = int(input("enter the key"))
    press = int(input("which element you want to print"))

    for i, j in d.items():
        try:
            if i == key:
                l += j[press - 1]
                print(j[press - 1])
        except Exception as e:
              print(e)

for i in l:
    str +=i
print(f"your string is:' {str} ' ")
