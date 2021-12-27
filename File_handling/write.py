file=open("textfile/b.txt", 'w+')

file.write("sssss")
file.write('good morning')
file.close()


#using with function

name=input("please enter your name")
age=int(input("Enter your age"))
ph_no=int(input("Enter your phone number"))
with open("textfile/b.csv", "a") as f:
      f.write(f"name :{name} \n")
      f.write((f" \nage:{age}\n"))
      f.write(f"\nph_no:{ph_no}\n")
      f.close()

with open("textfile/b.csv") as f:
     print(f.read())



