class Unit: # 부모클래스
    def __init__(self, name, hp, speed): #__init__은 클래스로 생성되는 객체의 초기값 역할.
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{}유닛 생성".format(self.name))

    def move(self, direction):
        print("{} : {}방향으로 {}속도로 이동중".format(self.name, direction, self.speed))

    def attacked(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("{} 유닛이 공격으로 죽었습니다".format(self.name))
        else:
            print("{} 유닛이 공격받았습니다. 받은 데미지는 {}이며, 남은 체력은 {}입니다".format(self.name, damage, self.hp))

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

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    def steampack(self): #일정시간동안 이속, 공격력 증가. 사용시 체력 10 감소
        if self.hp > 10:
            self.hp -= 10
            print("{} : 으아아! 힘이난다!".format(self.name))
        else:
            print("{} : 체력이 부족해 스팀팩 사용이 안됩니다".format(self.name))

class SeizeTank(AttackUnit):
    seizeMode = False

    def __init__(self):
        AttackUnit.__init__(self, "시즈탱크", 150, 1, 40)

    def seize(self): #시즈모드시 공격력 강화. 이동불가
        if SeizeTank.seizeMode == False:
            return
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
