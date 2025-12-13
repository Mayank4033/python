class developer:
    def __init__(self,language):
        self.language=language
    def code(self):
        print(f"i can learn {self.language}")
    def debug(self):
        print(f"i can debug {self.language}")

d1=developer('python')
d1.code()
d1.debug()