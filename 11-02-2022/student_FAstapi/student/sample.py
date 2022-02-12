import csv
def retrieve_csv():
    data=open('student_data.csv','r')
    l=['name','Kannad',"English",'Hindhi',"Maths","Science","Social"]
    l2=[]
    final_data=[]

    reader_file=csv.reader(data)
    for i in reader_file:
        l2.append(i)
    print(l2)

    for i in l2:
       for j in range(len(i)):
            d = {}
            if i[j].isdigit():
                j=int(j)
            d[l[j]]=i[j]
            final_data.append(d)

    print(final_data)
retrieve_csv()