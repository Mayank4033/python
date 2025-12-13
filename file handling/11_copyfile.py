import os 
import shutil

file_name  = input("enter file name to copy : ")
copyfile_name = input("enter another file name for copied file : ")

if not os.path.exists(file_name):
    print(f"{file_name} does not exist")
elif os.path.exists(copyfile_name):
    print(f"{copyfile_name} already exists,try another name")
else:
    shutil.copyfile(file_name,copyfile_name)
    print("file copied successfully!")
