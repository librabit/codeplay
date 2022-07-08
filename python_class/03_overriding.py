class Unit: # 부모클래스
    def __init__(self, name, hp, speed): #__init__은 클래스로 생성되는 객체의 초기값 역할.
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, direction):
        print("{} : {}방향으로 {}속도로 이동중".format(self.name, direction, self.speed))

class AttackUnit(Unit): #자식클래스
    def __init__(self, name, hp, speed, damage): #__init__은 클래스로 생성되는 객체의 초기값 역할.
        Unit.__init__(self, name, hp, speed)
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
        AttackUnit.__init__(self, name, 0, hp, damage)
        AirUnit.__init__(self, fly_speed)
    
    def move(self, direction):
        self.fly(self.name, direction)


vulture1 = AttackUnit("Vulture", 50, 10, 5)
battlecruiser1 = AirAttackUnit("Battle Cruiser", 300, 100, 5)

vulture1.move("11시")
# battlecruiser1.fly(battlecruiser1.name, "9시")
battlecruiser1.move("9시")