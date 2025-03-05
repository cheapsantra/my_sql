# DB connection bridge information
import mysql.connector as sq
connection = sq.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "my_dbprj"
    )

if connection.is_connected == False:
    print("connection failed")


def create_table():                     # function to create tables in DB : my_dbprj
    print('Entered create_table function !')
    cur = connection.cursor()
    t_name = input("enter table name: ")
    t_fields = input("enter the column and its datatype (max three): ")
    query = f"CREATE TABLE {t_name} ({t_fields});"
    print(f"Table '{t_name}' created successfully.")
    cur.execute(query)
    connection.commit()

def insert_records():                   #function to insert values into table
    print("Entered insert_records function! ")
    cur = connection.cursor()
    t_name = input("enter table name to insert into: ")
    t_values = input("enter the values (comma separated): ")
    query = f"INSERT INTO {t_name} VALUES ({t_values});"
    print(f"Records inserted into '{t_name}' successfully.")
    cur.execute(query)
    connection.commit()

def view_records():                      #function to view values of table
    print("Entered view_records function! ")
def list_tables():                       #function to list tables
    print("Entered list_tables function! ")
# main()
print('Student Database Record !')

while True:                             # Menu loop
    print('Press 1 : Creating Table.')
    print('Press 2 : Insert into Table.')
    print('Press 3 : View Records.')
    print('Press 4:List all tables.')
    print('Press 5 : Exit.')
    ch = input('Enter your choice : ')

    if ch == '1':                       # entering respective function
        create_table()
    elif ch == '2':
        insert_records()
    elif ch == '3':
        view_records()
    elif ch == '4':
        list_tables()
    elif ch == '5':
        break
    else :
        print('Wrong input, enter again !')# student database mysql