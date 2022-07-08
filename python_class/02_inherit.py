class Unit: # 부모클래스
    def __init__(self, name, hp): #__init__은 클래스로 생성되는 객체의 초기값 역할.
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #자식클래스
    def __init__(self, name, hp, damage): #__init__은 클래스로 생성되는 객체의 초기값 역할.
        Unit.__init__(self, name, hp)
        self.damage = damage
        print("{} 유닛이 생성되었습니다".format(self.name))
    
    def attack(self, direction):
        print("체력 : {}  |  공격력 : {}  |  공격방향 : {}".format(self.hp, self.damage, direction))

    def attacked(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("{} 유닛이 공격으로 죽었습니다".format(self.name))
        else:
            print("{} 유닛이 공격받았습니다. 받은 데미지는 {}이며, 남은 체력은 {}입니다".format(self.name, damage, self.hp))

class AirUnit:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, direction):
        print("{} : {}방향으로 {}속도로 이동중".format(self.name, direction, self.fly_speed))
    

class AirAttackUnit(AttackUnit, AirUnit): #다중상속. 쉼표로 구분
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, damage)
        AirUnit.__init__(self, fly_speed)

firebat = AttackUnit("Firebat", 50, 15)
firebat.attack("10시")
firebat.attacked(30)
firebat.attacked(30)

valkyrie1 = AirAttackUnit("Valkyrie", 300, 20, 5)
valkyrie1.fly(valkyrie1.name, "3시")
