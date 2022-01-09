
class Student:
     data = {}

     sub = ""
     total_marks = 0
     average = 0

     def data_user(self):
         obtn_mark = 0
         no_of_sub = int(input("Enter the no of subjects you registered : "))
         for i in range(no_of_sub):
            sub = input("enter the subject name")
            marks = int(input("enter the marks"))
            if (marks > 100):
                marks = int(input("please enter marks less than 100"))

            Student.data[sub] = marks
            total_marks = len(Student.data) * 100

         for i in Student.data.values():
            obtn_mark += i

         average = (obtn_mark / total_marks) * 100
         print(Student.data)

         high_mark = 0
         count = 0
         if no_of_sub <= 7:
            if average > 90:
                for i in Student.data.values():
                    if i >= 95:
                        count += 1
                        if count >= 3:
                            print("gold medal")
                            break
                print("distinction")

            elif (average > 75) and (average < 90):
                print("average")

            elif average < 75:
                cn = 0
                mk=0
                for i in Student.data.values():
                    if i < 75:
                        cn += 1
                        mk +=i
                        avg=(mk/(cn*100))*100
                if cn > 3 and avg<75:
                    print("failed")

                else:
                    print(avg,cn)
                    print("you have chance again")
                    Student.data.clear()
                    st = Student()
                    st.data_user()




         if no_of_sub > 7:
            if average > 90:
                for i in Student.data.values():
                    if i >= 95:
                        count += 1
                        if count >= 3:
                            print("gold medal")
                            break
                print("distinction")

            elif (average > 75) and (average < 90):
                print("average")


            elif average < 75:

                cn = 0

                mk = 0

                for i in Student.data.values():

                    if i < 75:
                        cn += 1

                        mk += i

                        avg = (mk / (cn * 100)) * 100

                if cn > 5 and avg < 75:

                    print("failed")


                else:

                    print("you have chance again")

                    Student.data.clear()

                    st = Student()

                    st.data_user()

std1 = Student()
std1.data_user()



