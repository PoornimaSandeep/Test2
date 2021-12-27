"""  craeating substring using constatnt and vovwels"""
from itertools import permutations,combinations

class combntn:
     str1 = 'namratha'
     vowels = ['a', 'e', 'i', 'o', 'u']
    # consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l''m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
     n_list = []
     A_len=0
     B_len=0
     def __init__(self):
         pass

     def combination_str(self,str):
         l = []
         for i in range(2, len(str)):
             l += permutations(str)
         for i in l:
             str = ''
             for item in i:
                 str = str + item
             combntn.n_list.append(str)
         print(combntn.n_list)

     def player_a(self):
         A_list = []
         d = {}
         for i in combntn.n_list:
             if i[0] in combntn.vowels:
                 A_list.append(i)
         #print(A_list)
         for i in A_list:
             if i not in d:
                 d[i] = 1
             elif i in d:
                 d[i] += 1
         combntn.A_len=len(d)
         print("A's substring are :",d)


     def player_b(self):
         B_list = []
         d = {}
         for i in combntn.n_list:
             if i[0] not in combntn.vowels:
                 B_list.append(i)
         #print(B_list)
         for i in B_list:
             if i not in d:
                 d[i] = 1
             elif i in d:
                 d[i] += 1
         combntn.B_len=len(d)
         print("B's substring are :", d)

     def display(self):

         if  combntn.A_len> combntn.B_len:

             print("A creating substring of :",combntn.A_len)
             print("A is winner")
         else:
             print("B creating substring of :", combntn.B_len)
             print("b is winner")

str=input("please enter the string")
cb=combntn()
cb.combination_str(str)
cb.player_a()
cb.player_b()
cb.display()
#str=input("enter the string")










#a=find_combinations()
#print(a)