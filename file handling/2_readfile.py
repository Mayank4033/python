name = input("enter filename to read : ")
mode = "r"

try:
    file = open(name,mode)
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("file not found")
else:
    print("file has been read successfully")