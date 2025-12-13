import os

try:
    c_name=input("enter existing file name to delete : ")
    os.remove(c_name)
    print("file deleted successfully!")
except FileNotFoundError:
    print(f"{c_name} is a folder or directory")
