import mysql.connector as sq
connection = sq.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "my_db"
    )

if connection.is_connected == False:
    print("connection failed")

uname = input("enter user name: ")
pswd = input("enter password: ")

cur = connection.cursor()
query = "insert into Login( UserName, Password) values (%s,%s);"

cur.execute(query,(uname,pswd))
connection.commit()

cur.execute("select *from Login;")
response = cur.fetchall()
for i in response:
    print(i)

print("data entered sucesfully!")

connection.close()