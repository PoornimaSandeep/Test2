import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",

                            password="postgress123")
    print("Connection object : ", type(conn), conn)

    # Step2 : Get cursor on db connection
    cursor = conn.cursor()
    print("Cursor object : ", type(cursor), cursor)

    # Step3: Prepare SQL Query
    query = "CREATE TABLE data2(chapter_no VARCHAR(1000), verse_no VARCHAR(1000) , language VARCHAR(1000),chapter_name VARCHAR(1000),verse VARCHAR(1000),transliteration VARCHAR(1000),synonyms VARCHAR(500),audio_link VARCHAR(1000),translation VARCHAR(1000))"


    # Step4 : Execute sql query
    cursor.execute(query)
# add repo commit remote
    # Step5: Commit the transaction
    conn.commit()

    print("** Table created successfully **")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()


