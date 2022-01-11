"""
You are given a positive integer .
Your task is to print a palindromic triangle of size .

For example, a palindromic triangle of size  is:
"""

size=int(input("Enter the size "))

for i in range(size):
    st=""
    for j in range(1,i+1):
        st +=str(j)
    print(f"{st}{st[::-1]}")
