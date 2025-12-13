import os

try:
    c_name=input("enter existing file name to rename : ")
    newname=input("enter new name : ")
    os.rename(c_name,newname)
    print("file renamed successfully!")
except FileNotFoundError:
    print(f"{c_name} is a folder or directory")
except FileExistsError:
    print(f"{newname} this filename already exists,try any other name!")
