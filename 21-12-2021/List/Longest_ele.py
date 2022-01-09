print("****** Words that are longer than any element *****")
l1=["poornima","suma","vishal","ranjan","sandeep","sowmya"]
dst={}

for i in l1:
    v=len(i)
    dst[i]=v
new_ele=max(dst.values())
for i,j in dst.items():
    if j==new_ele:
       print(f"Words that are longer than any element '{i}' and len of that element is '{j}'")

