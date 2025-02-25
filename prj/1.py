# student database mysql

# DB connection bridge information


def create_table():                     # function to create tables in DB : my_db
    print('Entered create_table function !')


# main()
print('Student Database Record !')

while True:                             # Menu loop
    print('Press 1 : Creating Table.')
    print('Press 2 : Insert into Table.')
    print('Press 5 : Exit.')
    ch = input('Enter your choice : ')

    if ch == '1':                       # entering respective function
        create_table()
    elif ch == '2':
        print('Insert value into table !')
    elif ch == '5':
        break
    else :
        print('Wrong input, enter again !')