import connect as con 
cursor = con.database.cursor(dictionary=True)
sql = "select * from person "
cursor.execute(sql)

# single = cursor.fetchone()
# print(single)

table = cursor.fetchall()
print(f"{'ID':<6} {'Name':<10} {'Salary':<10}  {'Mobile'}")
print('-'*39)
for row in table:
    output=f"{row['id']:<6} {row['name']:<10} {row['salary']:<10} {row['mobile_no']}"
    print(output)