class math:
    def getpi(self):
        pi = 3.14
        return pi
    def getsquare(self,num):
        square=num*num
        return square
class circle(math):
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        area = super().getpi()*super().getsquare(self.radius)
        return area
class square(math):
    def __init__(self,value):
        self.value=value
    def getarea(self):
        area = super().getsquare(self.value)
        return area
radius=float(input("enter radius : "))
c1=circle(radius)
print("area of circle is ",c1.getarea())
value=float(input("enter value of square : "))
s1=square(value)
print("area of square is ",s1.getarea())