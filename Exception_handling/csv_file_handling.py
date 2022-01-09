import csv

columns=['name','age','mobile_no']

rows=[['poornima',23,'9739935941'],['kavya',24,890909939333],['lll',26,59959059009]]

file= "textfile/student.csv"

try:
      with open(file, "w", newline="") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(columns)
            csvwriter.writerows(rows)

      with open(file, 'r') as f:
            csvreader = csv.reader(f)
            for i in csvreader:
                  print(i)
except Exception as e:
      print("exception occurs",e)



