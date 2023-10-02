class 캐릭터():
    def __init__(self, 체력, 공격력, 이속):
        self.체력 = 체력
        self.공격력 = 공격력
        self.이속 = 이속
    def 상태보기(self, name):
        print(name)
        print(f"체력 : {self.체력}")
        print(f"공격력 : {self.공격력}")
        print(f"이속 : {self.이속}")

class 챔피언(캐릭터):#캐릭터라는 클래스를 상속하여 서브클래스인 챔피언을 정의
    def __init__(self, 체력, 공격력, 이속, q, w, e, r):#부모 메서드를 업그레이드 하는것. 메서드 오버라이드
        super().__init__(체력, 공격력, 이속)
        self.q = q
        self.w = w
        self.e = e
        self.r = r  
    def 상태보기(self, name):
        super().상태보기(name)
        print(f"Q스킬 : {self.q}")
        print(f"W스킬 : {self.w}")
        print(f"E스킬 : {self.e}")        
        print(f"R스킬 : {self.r}")    

미니언01 = 캐릭터(100, 5, 20) #캐릭터라는 클래스로 미니언01이라는 인스턴스 생성
미니언01.상태보기("미니언1번의 상태") #미니언01 객체 안에 정의된 메서드Method(함수)를 호출
야스오 = 챔피언(100, 1000, 500, "찌르기", "장막", "돌진", "난도질") 
야스오.상태보기("야스오의 상태")

미니언01.체력 -= 야스오.공격력