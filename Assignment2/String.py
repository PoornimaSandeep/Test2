
class string_prb:

      def __init__(self):
          self.title=" string problem"
          self.first="1.count and display the vowels of a given text"
          self.second="2.capitalize first and last letters of each word of a given string"
          self.third="3.swap comma and dot in a string"
          self.four="4.program to check whether a string starts with specified characters"
          self.five="5.find length of given string"
          self.six="6.Count words in a string"
          self.seven="7.Count characters in a string"
          self.eight="8.convert string to upper and lowercase"


      def vowels_str(self):
          print("")
          print(self.first)
          str1=input("enter the string")
          v=["a","e",'i',"o","u"]
          count=0
          vow_str=[]
          for i in str1.lower():
              if i in v:
                  count+=1
                  vow_str.append(i)

          print (f"no of vovels in a string :{count}, string is :{vow_str}")



      def capitalize_first_last_letters(self,str1):
           print("")
           print( self.second)
           str1 = result = str1.title()
           result = ""
           for word in str1.split():
            result += word[:-1] + word[-1].upper() + " "
           print(result)

      def swap_comma_dot(self):
          print("")
          print(self.third)
          res=""
          str3="Each section gradually builds on the previous ones, but it's structured to. separate topics, so that you can go directly to any specific one to solve your specific API" " needs."
          print("before swap: ",str3)
          for i in str3:
              if(i==","):
                  i="."
              elif(i=="."):
                  i=","
              res +=i
          print("After swap :",res)

      def check_spec_char(self,str):
          print(" ")
          print(self.four)
          print(str)
          ch=input("enter the char which you are check")

          if ch==str[0]:
              print(f"YES ,the string start with {ch}")
          else:
              print(f"NO,the string not start with{ch}")


      def len_str(self,str):
          print(" ")
          print(self.five)
          print(str)
          print("length of string is ",len(str))

      def count_word(self):
          print(" ")
          print(self.six)
          str="directly to code any specific one to  code solve your specific API needs code code code code."
          print(str)
          print("count of code",str.count("code"))

      def count_char(self):
          print(" ")
          print(self.seven)
          str = "directly to code any specific one to  code solve your specific API needs code code code code."
          print(str)
          search="o"
          print(f"count of {search}", str.count(search))

      def str_upper(self):
          print(" ")
          print(self.eight)
          str="all the code blocks CAN  be copied AND used directly"
          print("upper case:",str.upper())


      def str_lower(self):
          print(" ")
          print("9.covert string to lowercase")
          str = "all the code blocks CAN  be copied AND used directly"
          print("lower case :", str.lower())

      def str_Capitalize(self):
          print(" ")
          print("10.string to upper case")
          str = "all the code blocks CAN  be copied AND used directly."
          print("Capitalize :", str.capitalize())


obj=string_prb()
obj.vowels_str()
obj.capitalize_first_last_letters("count and display the vowels of a given text")
obj.swap_comma_dot()
obj.check_spec_char("sandeep")
obj.len_str("GHHGdgvbd")
obj.count_word()
obj.count_char()
obj.str_upper()
obj.str_lower()
obj.str_Capitalize()
