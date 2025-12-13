import connect as con
cursor = con.database.cursor()
sql="insert into person(name,salary,mobile_no) values(%s,%s,%s)"
name = input("Enter Name : ")
salary=int(input("Enter salary : "))
mobile_no=input("Enter Mobile Number : ")

values=[name,salary,mobile_no]
cursor.execute(sql,values)
con.database.commit()
print(cursor.rowcount,"rows inserted!")
