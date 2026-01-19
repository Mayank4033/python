import connection as con
import shutil
columns  = shutil.get_terminal_size().columns
bill_total=0

print("Saral Billing Software".center(columns))
def display_bill_items():
    global bill_total
    bill_total=0
    sql="select i.id,productid,qty,p.price,name from item i,product p where i.productid=p.id and i.billid=0"
    table=con.fetch(sql)
    if len(table)==0:
        no_record_found()
    else:
        heading = f"{'ItemID':<8}{'Prod_ID':<8}{'Name':<20} {'Qty':<6} {'Price':<6} {'Total':<6}"
        print(heading)
        print("-" * len(heading))
        itemcount=0
        for row in table:
            itemtotal=row['qty']*row['price']
            output=f"{row['id']:<8} {row['productid']:<8}{row['name']:<20} {row['qty']:<6} {row['price']:<6} {itemtotal:<6}"
            print(output)
            bill_total=bill_total+(row['qty']*row['price'])
            print(bill_total)
        key=input("Press enter to continue...")
def input_with_default(message,current_value):
    user_input=input(f"{message} [{current_value}]: ").strip()
    return current_value if user_input=="" else user_input
def no_record_found():
    print("-"*columns)
    print("No Record Found".center(columns))
    print("-"*columns)
def display_products():
    search=input("Enter name to search product or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select id,name,price,stock,description,weight,size from product where isdeleted=0 limit %s,25"
            values=[start]
        else:
            search = f"%{search}%"
            sql="select id,name,price,stock,description,weight,size from product where isdeleted=0 and name like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Id':<5} {'Name':<25} {'Price':<6} {'Stock':<6} {'Description':<18} {'Weight':<10} {'Size':<6}")
            print('-'*columns)
            for row in table:
                output=f"{row['id']:<5} {row['name']:<25} {row['price']:<6} {row['stock']:<6} {row['description']:<18} {row['weight']:<10} {row['size']:<6}"
                print(output)
            start+=25
            key=input("Press enter to continue..")
        else:
            break
while True:
    print("Press 1 for Product Management")
    print("Press 2 for Bill Management")
    print("Press 0 for exit")
    choice = int(input("Enter your choice : "))
    if choice==1:
        print("Welcome to Product Management".center(columns))
        while True:
            print("Press 1 to view/search product")
            print("Press 2 to edit product")
            print("Press 3 to add new product")
            print("Press 4 to delete product")
            print("Press 0 to return main menu")
            product_choice=int(input("Enter your choice : "))
            if product_choice==1:
                display_products()
            elif product_choice==2:
                display_products()
                sql="select id,name,price,stock,description,weight,size from product where id=%s"
                product_id=int(input("Enter id to edit : "))
                values=[product_id]
                table=con.fetch(sql,values)
                if len(table)==0:
                    no_record_found()
                else:
                    # print("Type to change or press enter if no change")
                    name=input_with_default("Enter name",table[0]['name'])
                    price=input_with_default("Enter price",table[0]['price'])
                    stock=input_with_default("Enter stock",table[0]['stock'])
                    description=input_with_default("Enter description",table[0]['description'])
                    weight=input_with_default("Enter weight",table[0]['weight'])
                    size=input_with_default("Enter size",table[0]['size'])
                    sql="update product set name=%s,price=%s,stock=%s,description=%s,weight=%s,size=%s where id=%s"
                    values=[name,price,stock,description,weight,size,product_id]
                    con.run(sql,values,'Product Updated!')
            elif product_choice==3:
                try:
                    sql="insert into product(name,price,stock,description,weight,size) values(%s,%s,%s,%s,%s,%s)"
                    name=input("Enter name of product : ")
                    price=int(input("Enter price of product : "))
                    stock=int(input("Enter stock of product : "))
                    description=input("Enter description of product : ")
                    weight=float(input("Enter weight of product : "))
                    size=input("Enter size of product : ")
                    values=[name,price,stock,description,weight,size]
                    con.run(sql,values,'New Product Added!')
                except ValueError as e:
                    print("price,stock and weight must be in numbers")
            elif product_choice==4:
                display_products()
                product_id=int(input("Enter id to delete : "))
                sql="select id,name,price,stock,description,weight,size from product where id=%s"
                values=[product_id]
                table=con.fetch(sql,values)
                if len(table)==0:
                    no_record_found()
                else:
                    sql="update product set isdeleted=1 where id= %s "
                    values=[product_id]
                    con.run(sql,values,'Product Deleted!')
            elif product_choice==0:
                break
            else:
                print("invalid choice")
    elif choice==2:
        print("Welcome to Bill Management".center(columns))
        while True:
            print("Press 1 to add product into bill")
            print("Press 2 to view bill items ")
            print("Press 3 to delete  product from non print bill ")
            print("Press 4 to save and print bill")
            print("Press 5 to  get details of bill between given date ")
            print("Press 6 to search for specific bill by name")
            print("Press 0 to return main menu")
            product_choice=int(input("Enter your choice : "))
            if product_choice==1:
                display_products()
                productid = int(input("Enter product id : "))
                sql = 'select id,price,stock from product where id = %s'
                values = [productid]
                table = con.fetch(sql,values)
                if len(table) == 0:
                    display_no_record_found()
                else:
                    qty = int(input(f"Enter quantity [Available stock :{table[0]['stock']}]: "))
                    if qty>table[0]['stock']:
                        print("not enough stock, available stock is ",table[0]['stock'])
                        key=input("Press Enter to continue...")
                    else:
                        sql = "insert into item (productid,qty,price) values (%s,%s,%s)"
                        values = [productid,qty,table[0]['price']]
                        con.run(sql,values,'Item added into bill')
            elif product_choice==2:
                display_bill_items()
            elif product_choice==3:
                if bill_total==0:
                    no_record_found()
                else:
                    display_bill_items()
                    product_id=int(input("Enter item id to delete : "))
                    sql="select id from item where id=%s"
                    values=[product_id]
                    table=con.fetch(sql,values)
                    if len(table)==0:
                        no_record_found()
                    else:
                        sql="delete from item where id=%s"
                        values=[product_id]
                        con.run(sql,values,'Product Removed From Bill!')
            elif product_choice==4:
                '''
                1) generate bill (insert new row into bill table)
                2) update item table set billid using newly generated bill 
                3) update stock inside product table
                '''
                if bill_total==0:
                    no_record_found()
                else:
                    display_bill_items()
                    fullname=input("Enter customer fullname : ")
                    mobile=input("Enter mobile no : ")
                    mode=int(input("Enter mode of payment (1=cash,2=online,3=card,4=credit) : "))
                    sql="insert into bill(fullname,mobile,amount,mode) values(%s,%s,%s,%s)"
                    values=[fullname,mobile,bill_total,mode]
                    con.run(sql,values,'Bill Generated')
                    # 2
                    sql="select LAST_INSERT_ID() as last_bill_id from bill"
                    table=con.fetch(sql)
                    last_bill_id=table[0]['last_bill_id']
                    print(last_bill_id)
                    sql="update item set billid=%s where billid=0"
                    values=[last_bill_id]
                    con.run(sql,values,'Item table updated!')
            elif product_choice==5:
                print("get details of bill between dates")
            elif product_choice==6:
                print("search")
            elif product_choice==0:
                break
            else:
                print("invalid choice")
    elif choice==0:
        break
    else:
        print("invalid choice")