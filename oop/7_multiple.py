class exam :
    def getexaminfo(self):
        no=int(input("enter exam no : "))
        examname=input("enter exam name : ")
        return no,examname
class marks:
    def getmarks(self):
        marks=int(input("enter exam total marks : "))
        per = (marks/5)*100
        return marks
        
class student(exam,marks):
    def getinfo(self):
        rno = int(input("enter roll no of student : "))
        name=input("enter name of the student : ")
        return rno,name

s1 = student()
s1.getinfo()
s1.getexaminfo()
s1.getmarks()
print(f"roll no of student is {self.rno} \n name of student is {s1.name}")
print(f"exam no is {s1.no} and exam name is {s1.examname}")
print(f"percentage is {s1.per}")