
class company:

      data={}
      Salary_list={}
      Expenditure_list ={}
      Salary=0
      Expenditure=0

      def __init__(self):
          print("welcome")
      def Salary_acc(self):
          month = int(input("Enter the number of month"))
          for i in range(month):
              month = input("Enter month name")
              name_emp = input("enter your name")
              Emp_id = input("enter your employee id")
              print(" Salary details ")

              while(i==0):
                   salary_type=input("enter the salary feature")
                   amount=int(input("enter the amount "))
                   company.Salary_list[salary_type]=amount
                   i=int(input("you have more feature give 0 else 1"))

              exp=input("you have expenditure  'yes' or 'no' ")

              if exp =="yes":
                  j=0
                  while(j==0):
                      exp_name = input("enter the expenditure  name")
                      exp_amount = int(input("enter the amount "))
                      company.Expenditure_list[exp_name] = exp_amount
                      j = int(input("you have more feature give 0 else 1"))

              for i in company.Salary_list.values():
                   company.Salary +=i
              for i in company.Expenditure_list.values():
                  company.Expenditure+=i

              Total=company.Salary-company.Expenditure
              company.data[month]=Total
              if(Total>0):
                  print("winner")
              else:
                  print("looser")

              print(company.data)

com1=company()
com1.Salary_acc()
