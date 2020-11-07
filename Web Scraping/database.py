import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database = "entsoe"
)

mycursor = mydb.cursor()

mycursor.execute(("Create Table "))

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
