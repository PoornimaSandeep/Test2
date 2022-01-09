class functions_problems:

       def __init__(self):
           print("functions problems")


       def palindrome(self):
           print("")
           print("check given word is palindrome or not")
           str=input("please enter a string")
           str2=str[::-1]
           if str==str2:
               print(f"The given string {str2} is a palindrome")
           else:
               print(f"The given string {str2} is not a palindrome")

       def even_or_add(self):
           print("")
           print("print even and odd numbers")
           num=int(input("Enter the number :"))
           if num%2==0:
               print(f"{num} is even number")
           else:
               print(f"{num} is odd numbers")

       def prime_numbers(self):
           print("")
           print("print prime numbers")
           num=int(input("enter  number"))
           c=0;
           for i in range(1,num+1):
               if(num%i==0):
                   c +=1
           if(c==2):
              print(f"the number{num} is prime number")
           else:
               print(f"the number{num} is not prime number")

       def factorial_num(self):
           print("")
           print("Factorial numbers")
           dict={}
           def fact(n):
                if (n == 1 or n == 0):
                    return 1
                else:
                    return n * fact(n - 1)

           for i in range(1,9):
               dict[i]=fact(i)

           print("factorial number from 1to 8: ",dict)

       def square_and_cube(self):
           print("")
           print("find cube/square of a number")
           num="enter the number"
           print(num**num)
           print(num**num*num)

func_obj=functions_problems()
func_obj.palindrome()
func_obj.even_or_add()
func_obj.prime_numbers()
func_obj.factorial_num()