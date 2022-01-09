
class company:
      def __init__(self):
          print("welcome")

      data = {}

      def Salary_acc(self):
          month = int(input("Enter the number of month"))
          for i in range(month):
              month = input("Enter month name")
              name_emp = input("enter your name")
              Emp_id = input("enter your employee id")
              print("enter your salary details ")
              HRA = int(input("enter your HRA"))
              Basic = int(input("enter your basic salary"))
              Special_all = int(input("Enter your Special allownace"))
              Salary = HRA + Basic + Special_all
              esp_amount = 0
              exp = input("if you have any expenditure yes or no")
              if exp == "yes":
                  while (i == 0):
                      expenditure_name = input("Enter your expenditure")
                      esp_amount = int(input("Enter your amount"))
                      i = int(input("you have more expences please enter '0' else enter '1' "))

              Total = Salary - esp_amount
              company.data[month]=Total
              if (Total > 0):
                  print("you are winner ")
              else:
                  print("your are lose")

              print(company.data)
cm=company()
cm.Salary_acc()