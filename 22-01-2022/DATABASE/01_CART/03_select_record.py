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
    query = "SELECT * FROM cart"''
    cursor.execute(query)
    print("\n-----Retrieving records from db table Test-------")
    records = cursor.fetchall()
    for each in records:
        print(each)
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()