import mysql.connector as con
try:
    database = con.connect(host='localhost',user='root',passwd='',database='py30',port='3308')
    print("Database connection created...")
except con.Errors as e:
    print("Error in connection")
    print(e.errno)
    print(e.msg)