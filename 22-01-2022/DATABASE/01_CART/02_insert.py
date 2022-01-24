'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgress123",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    '''
    records = [(101, 'MADHU', 'ABC'), (102, 'Prakash', 'AREM'), (103, 'Kiran', 'VN2')]
    query = "INSERT INTO STUDENT VALUES(%s, %s, %s)"
    for record in records:
        cursor.execute(query, record)
    '''
    #Step3 : Prepare sql query
    rec1 = "INSERT INTO cart values(01, 'laptop', '40000')"
    rec2 = "insert into cart values(02, 'mobile', '30000')"
    rec3 = "insert into cart values(03, 'TV', '25000')"
    # Step4 : Execute sql query
    cursor.execute(rec1)
    cursor.execute(rec2)
    res = cursor.execute(rec3)
    print("Insertion : ", res)
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()