try:
    file = input("enter filename to write data : ")
    mode = "w"
    with open(file,mode)as f1:
        while True:
            name = input("enter your friend name to add (enter exit to stop): ")
            if (name=='exit'):
                break
            else:
                f1.write("\n"+name)
except PermissionError:
    print(f"{file}might be a folder or open in other software")