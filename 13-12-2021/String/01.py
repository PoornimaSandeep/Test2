class str_M_01:
      def __init__(self):
          print('Replace first occurance character  ')

      def replace(self):
          str="adcfgha"
          print(str)
          ch=input("please enter your character a want replace")
          ch2=input("please enter which character you replace")

          for i in range(len(str)):
             if str[i]==ch:
                 str2 = str.replace(ch, ch2,1)#(old,new,occurance/count)
                 print(str2)
                 break





st=str_M_01()
st.replace()