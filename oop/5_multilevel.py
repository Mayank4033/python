class person:
    def walk(self):
        super().talk()
        self.read()
class developer(student):
    def code(self):
        print("I can code and debug ")
    def cando(self):
        super().cando()
        self.code()
d1 = developer()
d1.cando()