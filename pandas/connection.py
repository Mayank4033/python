import mysql.connector as con
try:
    database=con.connect(host='localhost',user='root',passwd='',database='lecture_management',port='3308')
    print("Database connection established...")
except con.errors as e:
    print("Error in connection!")
    print(e.errno)
    print(e.msg)