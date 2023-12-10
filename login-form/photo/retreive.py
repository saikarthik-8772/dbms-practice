import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(name, photo):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='kathik',
                                             user='root',
                                             password='Karthik-337-')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from photo where name = %s"""

        cursor.execute(sql_fetch_blob_query, (name,))
        record = cursor.fetchall()
        for row in record:
            print("Name = ", row[0])
            image = row[1]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)


    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


readBLOB("karthik", r"C:\Users\Hp\Desktop\FlaskDemo\p.jpg")