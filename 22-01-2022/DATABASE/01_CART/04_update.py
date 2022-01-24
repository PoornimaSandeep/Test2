'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgress123",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    query = "UPDATE cart set product_name = 'hp laptop' where product_id = 01"
    res = cursor.execute(query)
    print("Record Updated successfully : ", res)
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()