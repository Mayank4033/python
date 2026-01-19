import connection as con
import shutil
columns=shutil.get_terminal_size().columns
def input_with_default(message,current_value):
    user_input=input(f"{message} [{current_value}]:")
    return current_value if user_input=="" else user_input
def no_record_found():
    print("No record found!")
    key=input("Press enter to continue")
def display_lecture_info():
    start=0
    while True:
        sql="select * from lecture where payment_id=0 limit %s,25"
        values=[start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Lecture_Id':<10} {'Teacher_Id':<10} {'Subject_Id':<10} {'Batch_Id':<10} {'Duration':<10} {'Amount':<15} {'Lecture_Date':<25}")
            print("-"*columns)
            for row in table:
                output=f"{row['lec_id']:<10} {row['teacher_id']:<10} {row['subject_id']:<10} {row['batch_id']:<10} {row['duration']:<10} {row['amount']:<15} {str(row['lec_date']):<25}"
                print(output)
            start+=25
            key=input("Press enter to continue.")
        else:
            if start==0:
                no_record_found()
            break
def display_teacher_info():
    search=input("Enter teacher name to search or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select * from teacher where isdeleted=0 limit %s,25"
            values=[start]
        else:
            search=f"%{search}%"
            sql="select * from teacher where isdeleted=0 and name like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Teacher_Id':<10} {'Name':<20} {'Mobile':<15} {'Email':<20} {'Gender':<8} {'Qualification':<20} {'Experience':<20}")
            print("-"*columns)
            for row in table:
                output=f"{row['teacher_id']:<10} {row['name']:<20} {row['mobile']:<15} {row['email']:<20} {row['gender']:<8} {row['qualification']:<20} {row['experience']:<20}"
                print(output)
            start+=25
            key=input("Press enter to continue.")
        else:
            if start==0:
                no_record_found()
            break
def display_subjects():
    search=input("Enter subject name to search or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select * from subject where isdeleted=0 limit %s,25"
            values=[start]
        else:
            search=f"%{search}%"
            sql="select * from subject where isdeleted=0 and title like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Sub_Id':<8} {'Course_Id':<10} {'Title':<30} {'Per_Hour_Rate':<6}")
            print("-"*columns)
            for row in table:
                output=f"{row['sub_id']:<8} {row['course_id']:<10} {row['title']:<30} {row['per_hour_rate']:<6}"
                print(output)
            start+=25
            key=input("Press enter to continue.")
        else:
            if start==0:
                no_record_found()
            break
def display_batches():
    search=input("Enter course name to search batch or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select b.batch_id,c.title,b.startdate,b.enddate,b.class_time from batch b,course c where b.course_id=c.id and b.isdeleted=0  limit %s,25"
            values=[start]
        else:
            search=f"%{search}%"
            sql="select b.batch_id,c.title,b.startdate,b.enddate,b.class_time from batch b,course c where b.course_id=c.id and b.isdeleted=0 and title like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Batch_id':<10} {'Course_Title':<30} {'Startdate':<10} {'Enddate':<10} {'Class_time':<10}")
            print("-"*columns)
            for row in table:
                output=f"{row['batch_id']:<10} {row['title']:<30} {str(row['startdate']):<10} {str(row['enddate']):<10} {row['class_time']:<10}"
                print(output)
            start+=25
            key=input("Press enter to continue.")
        else:
            if start==0:
                no_record_found()
            # print("Displayed All!")
            break
def display_courses():
    search=input("Enter course name to search or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select * from course where isdeleted=0 limit %s,25"
            values=[start]
        else:
            search=f"%{search}%"
            sql="select * from course where isdeleted=0 and title like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'ID':<6} {'Title':<25} {'Fees':<10} {'Duration':<10} {'Description':<6}")
            print("-"*columns)
            for row in table:
                output=f"{row['id']:<6} {row['title']:<25} {row['fees']:<10} {row['duration']:<10} {row['description']:<6}"
                print(output)
            start+=25
            key=input("Press enter to continue.")
        else:
            if start==0:
                no_record_found()
            break
print("Welcome to Lecture Payment Management System ".center(columns))
while True:
    try:
        print("Press 1 for Course Management ")
        print("Press 2 for Batch Management ")
        print("Press 3 for Subject Management ")
        print("Press 4 for Teacher Management ")
        print("Press 5 for Lecture Management ")
        print("Press 6 for Payment Management ")
        print("Press 7 to Get Reports ")
        print("Press 0 to exit ")
        choice = int(input("Enter your choice : "))
        if choice==1:
            while True:
                try:
                    print("Press 1 to insert course ")
                    print("Press 2 to update course ")
                    print("Press 3 to delete course ")
                    print("Press 4 to get details of course ")
                    print("Press 0 to return main menu")
                    choice=int(input("Enter your choice : "))
                    if choice==1:
                        sql="insert into course(title,fees,duration,description)values(%s,%s,%s,%s)"
                        title=input("Enter title of course : ")
                        fees=int(input("Enter fees :"))
                        duration=input("Enter duration : ")
                        description=input("Enter description : ")
                        values=[title,fees,duration,description]
                        con.run(sql,values,'Data inserted!')
                    elif choice==2:
                        display_courses()
                        id=int(input("Enter id to update record : "))
                        sql="select * from course where id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            title=input_with_default("Enter title  - ",table[0]['title'])
                            fees=input_with_default("Enter fees - ",table[0]['fees'])
                            duration=input_with_default("Enter duration - ",table[0]['duration'])
                            description=input_with_default("Enter description - ",table[0]['description'])
                            sql="update course set title=%s,fees=%s,duration=%s,description=%s where id=%s"
                            values=[title,fees,duration,description,id]
                            con.run(sql,values,'Row Updated!')
                    elif choice==3:
                        display_courses()
                        id = int(input("Enter id to delete record : "))
                        sql="select * from course where id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            sql="update course set isdeleted=1 where id=%s"
                            values=[id]
                            con.run(sql,values,'Record Deleted!')
                    elif choice==4:
                       display_courses()
                    elif choice==0:
                        break
                    else:
                        print("Invalid input")
                except ValueError:
                    print("Input cannot be empty and must be number(0-4)")
        elif choice==2:
            while True:
                try:
                    print("Press 1 to insert batch details ")
                    print("Press 2 to update batch details ")
                    print("Press 3 to delete batch details ")
                    print("Press 4 to get details of batch ")
                    print("Press 0 to return main menu")
                    choice=int(input("Enter your choice : "))
                    if choice==1:
                        sql="insert into batch(course_id,startdate,enddate,class_time)values(%s,%s,%s,%s)"
                        course_id=int(input("Enter course_id :"))
                        startdate=input("Enter startdate : ")
                        enddate=input("Enter enddate : ")
                        class_time=input("Enter class_time : ")
                        values=[course_id,startdate,enddate,class_time]
                        con.run(sql,values,'Data inserted!')
                    elif choice==2:
                        display_batches()
                        id=int(input("Enter id to update record : "))
                        sql="select * from batch where batch_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            course_id=input_with_default("Enter course_id  - ",table[0]['course_id'])
                            startdate=input_with_default("Enter startdate - ",table[0]['startdate'])
                            enddate=input_with_default("Enter enddate - ",table[0]['enddate'])
                            class_time=input_with_default("Enter class_time - ",table[0]['class_time'])
                            sql="update batch set course_id=%s,startdate=%s,enddate=%s,class_time=%s where batch_id=%s"
                            values=[course_id,startdate,enddate,class_time,id]
                            con.run(sql,values,'Row Updated!')
                    elif choice==3:
                        display_batches()
                        id = int(input("Enter id to delete record : "))
                        sql="select * from batch where batch_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            sql="update batch set isdeleted=1 where batch_id=%s"
                            values=[id]
                            con.run(sql,values,'Record Deleted!')
                    elif choice==4:
                        display_batches()
                    elif choice==0:
                        break
                    else:
                        print("Invalid Input!")
                except ValueError:
                    print("Input cannot be empty and must be number(0-4)")
        elif choice==3:
            while True:
                try:
                    print("Press 1 to insert subject details ")
                    print("Press 2 to update subject details ")
                    print("Press 3 to delete subject details ")
                    print("Press 4 to get details of subject ")
                    print("Press 0 to return main menu")
                    choice=int(input("Enter your choice : "))
                    if choice==1:
                        sql="insert into subject(course_id,title,per_hour_rate)values(%s,%s,%s)"
                        course_id=int(input("Enter course_id :"))
                        title=input("Enter title : ")
                        per_hour_rate=input("Enter per_hour_rate : ")
                        values=[course_id,title,per_hour_rate]
                        con.run(sql,values,'Data inserted!')
                    elif choice==2:
                        display_subjects()
                        id=int(input("Enter id to update record : "))
                        sql="select * from subject where sub_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            course_id=input_with_default("Enter course_id  - ",table[0]['course_id'])
                            title=input_with_default("Enter title - ",table[0]['title'])
                            per_hour_rate=input_with_default("Enter per_hour_rate - ",table[0]['per_hour_rate'])
                            sql="update subject set course_id=%s,title=%s,per_hour_rate=%s where sub_id=%s"
                            values=[course_id,title,per_hour_rate,id]
                            con.run(sql,values,'Row Updated!')
                    elif choice==3:
                        display_subjects()
                        id = int(input("Enter id to delete record : "))
                        sql="select * from subject where sub_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            sql="update subject set isdeleted=1 where sub_id=%s"
                            values=[id]
                            con.run(sql,values,'Record Deleted!')
                    elif choice==4:
                        display_subjects()
                    elif choice==0:
                        break
                    else:
                        print("Invalid Input!")
                except ValueError:
                    print("Input cannot be empty and must be number(0-4)")
        elif choice==4:
            while True:
                try:
                    print("Press 1 to insert teacher info ")
                    print("Press 2 to update teacher info ")
                    print("Press 3 to delete teacher info ")
                    print("Press 4 to get info of teacher ")
                    print("Press 0 to return main menu")
                    choice=int(input("Enter your choice : "))
                    if choice==1:
                        sql="insert into teacher(name,mobile,email,gender,qualification,experience)values(%s,%s,%s,%s,%s,%s)"
                        name=input("Enter name : ")
                        mobile=input("Enter mobile : ")
                        email=input("Enter email : ")
                        gender=input("Enter gender(m or f) : ")
                        qualification=input("Enter qualification : ")
                        experience=input("Enter experience : ")
                        values=[name,mobile,email,gender,qualification,experience]
                        con.run(sql,values,'Data inserted!')
                    elif choice==2:
                        display_teacher_info()
                        id=int(input("Enter id to update record : "))
                        sql="select * from teacher where teacher_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            name=input_with_default("Enter name  - ",table[0]['name'])
                            mobile=input_with_default("Enter mobile  - ",table[0]['mobile'])
                            email=input_with_default("Enter email  - ",table[0]['email'])
                            gender=input_with_default("Enter gender  - ",table[0]['gender'])
                            qualification=input_with_default("Enter qualification  - ",table[0]['qualification'])
                            experience=input_with_default("Enter experience  - ",table[0]['experience'])
                            sql="update teacher set name=%s,mobile=%s,email=%s,gender=%s,qualification=%s,experience=%s where teacher_id=%s"
                            values=[name,mobile,email,gender,qualification,experience,id]
                            con.run(sql,values,'Row Updated!')
                    elif choice==3:
                        display_teacher_info()
                        id = int(input("Enter id to delete record : "))
                        sql="select * from teacher where teacher_id=%s"
                        values=[id]
                        table=con.fetch(sql,values)
                        if len(table)==0:
                            no_record_found()
                        else:
                            sql="update teacher set isdeleted=1 where teacher_id=%s"
                            values=[id]
                            con.run(sql,values,'Record Deleted!')
                    elif choice==4:
                        display_teacher_info()
                    elif choice==0:
                        break
                    else:
                        print("Invalid Input!")
                except ValueError:
                    print("Input cannot be empty and must be number(0-4)")
        elif choice==5:
            while True:
                try:
                    print("Press 1 to insert lecture detail")
                    print("Press 2 to get lecture detail")
                    print("Press 0 to return main menu")
                    choice=int(input("Enter your choice : "))
                    if choice==1:
                        sql1="insert into lecture(teacher_id,subject_id,batch_id,duration,amount,lec_date) values(%s,%s,%s,%s,%s,%s)"
                        display_teacher_info()
                        teacher_id=int(input("Enter Teacher_id : "))
                        sql="select teacher_id from teacher where isdeleted=0 and teacher_id=%s"
                        values=[teacher_id]
                        table=con.fetch(sql,values)
                        if len(table)>0:                    
                            display_subjects()    
                            subject_id=int(input("Enter Subject_id : "))
                            sql="select sub_id from subject where isdeleted=0 and sub_id=%s"
                            values=[subject_id]
                            table=con.fetch(sql,values)
                            if len(table)>0:
                                display_batches()
                                batch_id=int(input("Enter Batch_id : "))
                                sql="select batch_id from batch where isdeleted=0 and batch_id=%s"
                                values=[batch_id]
                                table=con.fetch(sql,values)
                                if len(table)>0:
                                    cursor=con.database.cursor()
                                    duration=int(input("Enter duration in hours : "))
                                    lec_date=input("Enter Lecture Date(yyyy-mm-dd) : ")

                                    rate="select per_hour_rate from subject where sub_id=%s"
                                    values=[subject_id]
                                    result=con.fetch(rate,values)
                                    per_hour_rate=result[0]['per_hour_rate']
                                    print("Per Hour Rate : ",per_hour_rate)
                                    amount=per_hour_rate*duration
                                    values=[teacher_id,subject_id,batch_id,duration,amount,lec_date]
                                    con.run(sql1,values,'Data Inserted!')
                                else:
                                    print("Batch Id not found,enter valid id")
                            else:
                                print("Subject Id not found,enter valid id")
                        else:
                            print("Teacher Id not found,enter valid id")
                    elif choice==2:
                        display_lecture_info()
                    elif choice==0:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Input cannot be empty and must be numbers(0-2)")
        elif choice==6:
            sql1="insert into payment(payment_date,teacher_id,amount)values(%s,%s,%s)"
            try:
                teacher_id=int(input("Enter Teacher Id : "))
                sql="select teacher_id,amount from lecture where payment_id=0 and  teacher_id=%s"
                values=[teacher_id]
                table=con.fetch(sql,values)
                if len(table)>0:
                    date=input("Enter Payment Date : ")
                    amount=0
                    for row in table:
                        amount+=row['amount']
                    print("Total Amount : ",amount)
                    choice=input("Do Payment(y/n)? : ").lower()
                    if choice=='y':
                        values=[date,teacher_id,amount]
                        print("Payment Done!")
                        con.run(sql1,values,'Data Inserted!')
                        sql="select LAST_INSERT_ID() AS last_payment_id from payment"
                        table=con.fetch(sql)
                        last_payment_id=table[0]['last_payment_id']
                        print("Payment_ID : ",last_payment_id)
                        sql="update lecture set payment_id=%s where teacher_id=%s"
                        values=[last_payment_id,teacher_id]
                        con.run(sql,values,'Lecture Table Updated!')
                    else:
                        key=input("Press enter to return main menu.")
                else:
                    no_record_found()
            except ValueError:
                print("Input cannot be empty and also not string!")
        elif choice==7:
            while True:
                print("Press 1 to generate batch wise lecture detail between given date")
                print("Press 2 generate batch wise lecture detail with total amount")
                print("Press 0 to return main menu ")
                choice=int(input("Enter your choice : "))
                if choice==1:
                    display_batches()
                    id=int(input("Enter batch id : "))
                    sql="select batch_id from lecture where batch_id=%s"
                    values=[id]
                    table=con.fetch(sql,values)
                    if len(table)==0:
                        no_record_found()
                    else:
                        date1=input("Enter starting date : ")
                        date2=input("Enter ending date : ")
                        sql="select l.lec_id,count(l.batch_id)as batch_id,c.title from lecture l,course c,batch b where l.batch_id=b.batch_id and b.course_id=c.id and l.batch_id=%s and l.lec_date between %s and %s"
                        values=[id,date1,date2]
                        table=con.fetch(sql,values)
                        result=table[0]['batch_id']
                        print(f"{'Lecture_id':12} {'Batch_Name':25 } {'Total_Lectures':15}")
                        print("-"*columns)
                        for row in table:
                            output=f"{row['lec_id']:12} {row['title']:25} {result:15}"
                            print(output)
                elif choice==0:
                    break
                else:
                    print("Invalid Choice!")
        elif choice==0:
            break
        else:
            print("Invalid input")
    except ValueError:
        print("Input cannot be empty and must be numbers(0-7)!")