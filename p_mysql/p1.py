import mysql.connector as sq
connection = sq.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="my_db"
    )

if connection.is_connected() == False:
    print("not connected.")

cur = connection.cursor()
cur.execute("select * from Employee;")
response = cur.fetchall()
for i in response:
    print(i)

connection.close()