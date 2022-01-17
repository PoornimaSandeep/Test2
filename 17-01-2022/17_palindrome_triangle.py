for i in range(1, 5 + 1):
    st = ""
    for j in range(1, i + 1):
        st += str(j)

    print(f'{st}{st[-2::-1]}')

print("")
print("using list compression")
l = [[j for j in range(1, i + 1)] for i in range(1, 4 + 1)]
print("list",l)
for i in l:
    stx = ""
    for j in i:
        stx += str(j)
    print(f'{stx}{stx[-2::-1]}')


