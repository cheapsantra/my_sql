# using while loop and fetch one, fetch all details from table employee

import mysql.connector as sq
connection = sq.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "my_db"
    )

if connection.is_connected == False:
    print("not connected")

uname = input('Enter user name : ')
upass = input('Enter password : ')

cur = connection.cursor()

query = "insert into Login (UserName , Password) values (%s, %s)"
cur.execute(query,(uname,upass))

print('Data entered successfully !')

connection.close()