def swap_f_l():
    print("First last chars swapping")
    str=input("please enter the value")
    st=str.split()
    for i in st:
        l=len(i)-1
        print(i[l]+i[1:l]+i[0], end=" ")

swap_f_l()