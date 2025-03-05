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
        print('Enter into myconnect.')
        c_execute.execute("create table login")
        print('Table created !')
        

except :
    print("couldn't connect to database.")
