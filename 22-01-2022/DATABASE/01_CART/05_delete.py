'''
Created on Mar 20, 2020

@author: madhu

UI --> Python --> Database

'''
import psycopg2
try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgress123",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    product_id = int(input("Enter product id : "))
    cursor.execute("DELETE FROM cart WHERE product_id = {0}".format(product_id))
    print("Deleted record successfully")
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()