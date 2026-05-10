# write a program to create function getMerit that has 5 input maths, science, english, gujarati, hindi. this function will display total of all subject, average and return math and science which will decide merit of student as per blow criteria 
#  if total above 180 student can take B Group
#  if total above 160 student can take A Group
#  if total above 140 student can take admission in diploma
#  if total above 120 student can take admission in Bsc
#  if total below 120 student can take admission else

def getMerit(maths,hindi,gujarati,english,science):
    total = maths + hindi + gujarati + english + science;
    average = total/5;
    merittotal= maths + science;
    print("all subjects total : ",total)
    print("all subjects average : ",average)
    print(f"maths {maths}, science {science}, english {english}, gujarati {gujarati}, hindi {hindi}")
    return merittotal;

m    = int(input("Enter Maths marks: "))
c  = int(input("Enter Science marks: "))
e  = int(input("Enter English marks: "))
g = int(input("Enter Gujarati marks: "))
h    = int(input("Enter Hindi marks: "))
merit=getMerit(maths=m,gujarati=g,hindi=h,english=e,science=c,)
print(merit)
