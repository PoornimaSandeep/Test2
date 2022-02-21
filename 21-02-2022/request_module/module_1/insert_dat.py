import psycopg2
import  main

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgress123",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()

    records = main.dict
    query = "INSERT INTO data(chapter_no, verse_no , language,chapter_name,verse ,transliteration ," \
            "synonyms ,audio_link ,translation) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s)"


    lst=[]
    for key,value in records.items():
        if key=='purport':
            continue
        else:
            lst.append(value)
    t=tuple(lst)
    cursor.execute(query, t)

    #Step3 : Prepare sql query

    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()