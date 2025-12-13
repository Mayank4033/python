class person:
    def walk(self):
        print("i can walk")
    def talk(self):
        print("i can talk")

class student(person):
    def read(self):
        print("i cann read")
    def cando(self):
        super().walk()
        super().talk()
        self.read()

s1=student()
s1.cando()