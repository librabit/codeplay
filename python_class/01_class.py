# # # 마린 : 공격유닛, 전사, 칼질
# # name = "marine"
# # hp = 100
# # damage = 10

# # print("{} 유닛이 생성되었습니다.".format(name))
# # print("체력 : {}  |  공격력 : {}".format(hp, damage))

# # #시즈탱크 : 공격유닛, 기계, 통통포 / 시즈모드 공격 두개 가능
# # tank_name = "seize tank"
# # tank_hp = 200
# # tank_damage = 50

# # print("{} 유닛이 생성되었습니다.".format(tank_name))
# # print("체력 : {}  |  공격력 : {}".format(tank_hp, tank_damage))

# # def attack(name, direction, damage):
# #     print("{} : {} 쪽으로 공격중 [공격력 : {}]".format(name, direction, damage))

# # attack(name, "1시", damage)
# # attack(tank_name, "9시", tank_damage)

# # 이렇게 게임 내에 등장하는 등장인물이 많아지다 보면 변수가 몇십 몇백에 달하는....
# # 비슷하지만 다른 개체들을 도장찍듯 찍어내서 관리할 순 없을까?
# # 그거시 바로 클래스! 틀을 만들고, 찍어내면 된다?!

# class Unit:
#     def __init__(self, name, hp, damage): #__init__은 클래스로 생성되는 객체의 초기값 역할.
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다".format(self.name))
#         print("체력 : {}  |  공격력 : {}".format(self.hp, self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage): #__init__은 클래스로 생성되는 객체의 초기값 역할.
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다".format(self.name))
    
#     def attack(self, direction):
#         print("체력 : {}  |  공격력 : {}  |  공격방향 : {}".format(self.hp, self.damage, direction))

#     def attacked(self, damage):
#         self.hp -= damage
#         if self.hp <= 0:
#             print("{} 유닛이 공격으로 죽었습니다".format(self.name))
#         else:
#             print("{} 유닛이 공격받았습니다. 받은 데미지는 {}이며, 남은 체력은 {}입니다".format(self.name, damage, self.hp))

# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# tank1 = Unit("Seize Tank", 200, 50)
# tank2 = Unit("Seize Tank", 200, 50)
# wraith1 = Unit("Wraith", 50, 10)
# #클래스 내부의 변수를 외부에서 뽑아쓸 때는 객체명에 점을 찍고 변수명을 적어주면 된다. 이걸 멤버변수라고 함.
# print("방금 뽑은 유닛은 {}이고, 체력과 공격력은 각각 {}/{} 입니다".format(wraith1.name, wraith1.hp, wraith1.damage))
# wraith2 = Unit("Clocking Wraith", 50, 10)
# wraith2.clocking = True #클래스 안에는 없었지만, 외부에서 멤버변수를 추가할 수도 있음. 이건 지금만든 객체에만 적용

# if wraith2.clocking == True:
#     print("{}는 현재 클로킹중입니다".format(wraith2.name))

# firebat = AttackUnit("Firebat", 50, 15)
# firebat.attack("10시")
# firebat.attacked(30)
# firebat.attacked(30)






# class 참치선물세트:
#     일반 = 0
#     야채 = 0
#     고추 = 0

#     def 총합(self, 이름):
#         내용물갯수 = self.일반 + self.야채 + self.고추
#         print(이름 + str(내용물갯수) + "개")

#     def 출력(self):
#         self.총합("담긴 참치 갯수 : ")

# 참치1호 =  참치선물세트()
# 참치1호.일반 = 5
# 참치1호.야채 = 3
# 참치1호.고추 = 2

# 참치1호.출력()


class 참치선물세트():
    def __init__(self, 일반, 야채, 고추, 스킬):
        self.normal = 일반
        self.vege = 야채
        self.pepper = 고추
        self.skill = 스킬

    def 내용물보기(self, name):
        print(name)
        print("일반참치 : " + str(self.normal))
        print("야채참치 : " + str(self.vege))
        print("고추참치 : " + str(self.pepper))
        print("스킬들 : ", self.skill.values())    

참치1호 = 참치선물세트(10, 3, 4, {"q" : "질풍참", "w" : "보호막", "e" : "참수"})
참치1호.내용물보기("참치1호 내용물 안내")

print(type(참치1호))

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

# yasuo.hp -= timo.damage

# print(yasuo.hp)
