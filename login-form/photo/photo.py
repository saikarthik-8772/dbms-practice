import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

print("hello")
def insertBLOB( name, photo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='kathik',
                                             user='root',
                                             password='Karthik-337-')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO photo
                          (name, pic) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(photo)
        

        # Convert data into tuple format
        insert_blob_tuple = ( name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB("karthik", r"C:\Users\Hp\Desktop\FlaskDemo\photo\photo.jpg")
