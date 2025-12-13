import connect as con
cursor=con.database.cursor()
sql="delete from person where id=%s"
id = int(input("Enter id to delete : "))
values=[id]
cursor.execute(sql,values)
con.database.commit()
print(cursor.rowcount,'rows deleted')