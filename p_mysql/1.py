import mysql.connector as sq 
mydb = None

try:
    mydb = sq.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="my_db"
    )

    if mydb.is_connected():
        c_execute = mydb.cursor()
        c_execute.execute("SELECT * from Students;")
        record = c_execute.fetchall()
        print("you are connected to database: ", record)

except :
    print("couldn't connect to database.")
