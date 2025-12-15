import connection as con
import shutil

columns=shutil.get_terminal_size().columns
print("Saral Billing Software".center(columns))
def display_no_record_found():
    print("-"*columns)
    print("No Record Found!".center(columns))
    print("-"*columns)
def input_with_default(message,current_value):
    user_input=input(f"{message} [{current_value}] :").strip()
    return current_value if user_input=="" else user_input
def display_products():
    search=input("Enter name to search product or press enter to view all : ")
    start=0
    while True:
        if len(search)==0:
            sql="select id,name,price,stock,description,size from product limit %s,25"
            values=[start]
        else:
            search = f"%{search}%"
            sql="select id,name,price,stock,description,size from product where name like %s limit %s,25"
            values=[search,start]
        table=con.fetch(sql,values)
        if len(table)>0:
            print(f"{'Id':<5} {'Name':<25} {'Price':<6} {'Stock':<6} {'Description':<18} {'Size':<6}")
            print('-'*columns)
            for row in table:
                output=f"{row['id']:<5} {row['name']:<25} {row['price']:<6} {row['stock']:<6} {row['description']:<18} {row['size']:<6}"
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
        print("Welcome to Product Management")
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
                product_id=int(input("Enter product id to edit : "))
                sql="select id,name,price,stock,description,size from product where id=%s"
                values=[product_id]
                table=con.fetch(sql,values)
                if len(table)==0:
                    display_no_record_found()
                else:
                    name=input_with_default("Enter name : ",table[0]['name'])
                    price=input_with_default("Enter price : ",table[0]['price'])
                    stock=input_with_default("Enter stock : ",table[0]['stock'])
                    description=input_with_default("Enter description : ",table[0]['description'])
                    size=input_with_default("Enter size : ",table[0]['size'])
                    sql="update product set name=%s,price=%s,stock=%s,description=%s,size=%s where id=%s"
                    values=[name,price,stock,description,size,product_id]
                    con.run(sql,values,'Product Updated!')
            elif product_choice==3:
                try:
                    sql="insert into product(name,price,stock,description,size) values(%s,%s,%s,%s,%s)"
                    name=input("Enter name of product : ")
                    price=int(input("Enter price of product : "))
                    stock=int(input("Enter stock of product : "))
                    description=input("Enter description of product : ")
                    size=input("Enter size of product : ")
                    values=[name,price,stock,description,size]
                    con.run(sql,values,'New Product Added!')
                except ValueError as e:
                    print("price and stock must be in numbers")
            elif product_choice==4:
                print("delete")
            elif product_choice==0:
                break
            else:
                print("invalid choice")
    elif choice==2:
        print("Welcome to Bill Management")
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
                print("add product into bill")
            elif product_choice==2:
                print("view bill items")
            elif product_choice==3:
                print("delete  product")
            elif product_choice==4:
                print("save and print bill")
            elif product_choice==5:
                print("get details of bill")
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