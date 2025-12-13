import mysql.connector as con
import mysql
try:
    database = con.connect(host='localhost',user='root',passwd='',database='shop',port='3308')
    print("Database connection created...")
except con.Errors as e:
    print("Error in connection")
    print(e.errno)
    print(e.msg)

def run(sql,values,message):
    try:
        cursor=database.cursor()
        cursor.execute(sql,values)
        database.commit()
        print(message)
        print("Press enter to continue...")
    except mysql.connector.errors.ProgrammingError as error:
        print("oops something went wrong!")
        print(error)
def fetch(sql,values=None):
    try:
        cursor=database.cursor(dictionary=True)
        if values==None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,values)
        table = cursor.fetchall()
        return table
        print("Done")
    except mysql.connector.errors.ProgrammingError as error:
        print("oops something went wrong!")
        print(error)
        return None