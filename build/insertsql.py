import mysql.connector

def insert_values(sql,values):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="HospitalManagement"
    )
    cursor = conn.cursor()
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as error:
        print(f"Error inserting record: {error}")
    cursor.close()
    conn.close()
