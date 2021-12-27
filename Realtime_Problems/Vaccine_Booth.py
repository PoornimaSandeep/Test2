class vaccine_booth:

      def __init__(self):
          print("India's  Vaccination Portal")

      def vaccine(self):
          Vaccine_dict={}
          type_vaccine=["Dose1","Dose2"]
          i=1
          while i>0:
              Adhar_no = int(input("Enter Your Adhar number"))
              if Adhar_no not in Vaccine_dict.keys():
                  name = input("Enter Your name")
                  DOB = int(input("enter your birth year"))
                  vaccine_type = "Dose1"
                  age = 2021 - DOB
                  if age > 17:
                      Vaccine_dict[Adhar_no] = [name,age,vaccine_type]
                      print(Vaccine_dict)

                  else:
                      print("Sorry, your are not eleigible for vaccination")
              elif vaccine_type=='Dose1':
                   for i, j in Vaccine_dict.items():
                       if Adhar_no==i:
                           if vaccine_type in j:
                               print("you are already vaccinated of dose1 ,now you are eligible for Dose2")
                               vaccine_type="Dose2"
                               Vaccine_dict[Adhar_no]=[vaccine_type]
              else:
                   print("Your already Vaccinated")
              a = input("Still you have more people  yes else no")
              if a == 'yes':
                  i=1
              else:
                  i=0


vb=vaccine_booth()

vb.vaccine()

