class student:
    college = "SSCCS"
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print(f"name is {self.name} and roll no is {self.rno}")
s1=student("mayank",111)
s1.display()
print("college name is : "+s1.college)