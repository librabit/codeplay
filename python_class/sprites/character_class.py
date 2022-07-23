class 캐릭터():
    def __init__(self, 체력, 공격력, 이속):
        self.체력 = 체력
        self.공격력 = 공격력
        self.이속 = 이속

    def 상태보기(self, name):
        print(name)
        print("체력 : {}".format(self.체력))
        print("공격력 : {}".format(self.공격력))
        print("이속 : {}".format(self.이속))

class 챔피언(캐릭터):
    def __init__(self, 체력, 공격력, 이속, q, w, e, r):
        super().__init__(체력, 공격력, 이속)
        self.q = q
        self.w = w
        self.e = e
        self.r = r
    
    def 상태보기(self, name):
        super().상태보기(name)
        print("Q스킬 : {}".format(self.q))
        print("W스킬 : {}".format(self.w))
        print("E스킬 : {}".format(self.e))        
        print("R스킬 : {}".format(self.r))

print(dir(챔피언))