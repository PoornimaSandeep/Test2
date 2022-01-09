print("program to check whether a string starts with specified characters")
str=input("enter the string")

def check_spec_char(str):
    ch = input("enter the char which you are check")

    if ch == str[0]:
        print(f"YES ,the string start with {ch}")
    else:
        print(f"NO,the string not start with{ch}")

check_spec_char(str)