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

class 챔피언(캐릭터):
    def __init__(self, 체력, 공격력, 이속, q, w, e, r):
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

미니언01 = 캐릭터(100, 5, 20)
미니언01.상태보기("미니언1번의 상태")
야스오 = 챔피언(100, 1000, 500, "찌르기", "장막", "돌진", "난도질")
야스오.상태보기("야스오의 상태")

characters = []
characters.append("abc")


# # def jammini():
# #     print("아싸라비야 콜롬비야")

# # name = "코딩쌤"
# # age = 10
# # like = ["과메기", "육회", "대방어"]
# # hamsu = jammini

# # print(type(jammini), type(name), type(age), type(like), type(hamsu))


#코딩에서의 함수 : 하나의 소스코드 파일 안에서 동작하는 작은 프로그램
#파이썬 코딩에서의 클래스 : 모든 대상을 객체object로 만드는 방법

class 참치선물세트:
    일반 = 0
    야채 = 0
    고추 = 0

spam = 참치선물세트()
print(type(spam))

spam.일반 = 5
spam.야채 = 1
spam.고추 = 7

print(dir(spam), spam.일반 + spam.야채 + spam.고추)



# # class Units:
# #     hp = 0
# #     damage = 0
# #     speed = 0


    
# # timo = Units()
# # timo.hp = 10
# # timo.damage = 100
# # timo.speed = 50

# # yasuo = Units()
# # yasuo.hp = 5
# # yasuo.damage = 1000
# # yasuo.speed = 100

# # print(f"티모 - 체력 : {timo.hp} | 공격력 : {timo.damage} | 이속 : {timo.speed}")
# # print(f"야스오 - 체력 : {yasuo.hp} | 공격력 : {yasuo.damage} | 이속 : {yasuo.speed}")


# class 참치선물세트:
#     일반 = 0
#     야채 = 0
#     고추 = 0

#     def 총합(self, 이름):
#         내용물갯수 = self.일반 + self.야채 + self.고추
#         print(이름 + str(내용물갯수))
# 참치1호 = 참치선물세트()
# 참치1호.일반 = 5
# 참치1호.야채 = 3
# 참치1호.고추 = 2

# 참치갯수 = 참치1호.총합("담긴 참치 갯수 : ")

# print(참치갯수)


class 참치선물세트:
    # 클래스 안에 정의된 데이터들
    일반 = 0
    야채 = 0
    고추 = 0
    제조정보 = []
    # 클래스 안에 정의된 함수들
    def 총합(self, 이름):
        내용물갯수 = self.일반 + self.야채 + self.고추
        print(이름 + str(내용물갯수) + "\n" + " / ".join(self.제조정보))
    def 출력(self):
        self.총합("담긴 참치 갯수 : ")
참치3호세트 = 참치선물세트()
참치3호세트.일반 = 11
참치3호세트.야채 = 3
참치3호세트.고추 = 3
참치3호세트.제조정보.append("2020. 1. 1")
참치3호세트.제조정보.append("백두산 참치공장")
참치3호세트.제조정보.append("제조책임 - 김정은")
참치3호세트.총합("몇개니? : ")

# class Units:
#     hp = 0
#     damage = 0
#     speed = 0

# timo = Units()
# timo.hp = 10
# timo.damage = 100
# timo.speed = 50

# yasuo = Units()
# yasuo.hp = 5
# yasuo.damage = 1000
# yasuo.speed = 100

# print(f"티모 - 체력 : {timo.hp} | 공격력 : {timo.damage} | 이속 : {timo.speed}")