import connect as con
cursor = con.database.cursor()
sql="update person set name=%s,salary=%s,mobile_no=%s where id = %s"
id = int(input("Enter id to update data : "))
name = input("Enter Name : ")
salary=int(input("Enter salary : "))
mobile_no=input("Enter Mobile Number : ")

values=[name,salary,mobile_no,id]
cursor.execute(sql,values)
con.database.commit()
print(cursor.rowcount,"rows updated!")