filename="geet.txt"
mode="r"
with open(filename,mode) as file:

    for res in file:
        print(res.strip())
    
file.close()