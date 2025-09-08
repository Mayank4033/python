a = int(input("enter marks : "))

if(a<33):
    print("fail!")
else:
    if a<=100 and a>85:
        print("A grade!")
    elif a<=85 and a>70 :
        print("B grade!")
    elif a<=70 and a>55:
        print("C grade!")
    elif a<=55 and a>40:
        print("D grade!")
    else:
        print("E grade!")        