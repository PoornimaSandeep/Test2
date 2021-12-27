class pld:

     def __init__(self):
         print("check given word is palindrome or not")

     def palindrome(self):
         str = input("please enter a string")
         str2 = str[::-1]
         if str == str2:
             print(f"The given string {str2} is a palindrome")
         else:
             print(f"The given string {str2} is not a palindrome")

p=pld()
p.palindrome()