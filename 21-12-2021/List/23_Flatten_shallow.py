print("Flatten shallow")
l=[[23,45,66],[6868,90],[68,76,896]]
flatten_list=[]

for i in l:
     for j in i:
        flatten_list.append(j)
print(flatten_list)
