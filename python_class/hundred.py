class human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = human("엄정호", 100, "중성")

areum.who()
areum.setInfo('주찬', 3, "염기성")
areum.who()