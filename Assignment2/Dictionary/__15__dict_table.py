class dict_table:
       def __init__(self):
           print("Print a dictionary in table format. ")

       def table_dict(self):
           d={'name':'adress','poornima':'Tumkur','Rakshitha':'bangalore','Sandeep':'Madugiri'}
           for i,j in d.items():
               print("{:<15}{:<15}".format(i,j))

dt=dict_table()
dt.table_dict()