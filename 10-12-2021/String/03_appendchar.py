class appendchar:
    def __init__(self):
        print("Append chars to string at end")

    def append_char(self,str2):
        str="hello"

        str +=str2
        print(str)
ap=appendchar()
str2=input("enter the char")
ap.append_char(str2)