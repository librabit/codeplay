점화 = 300

class Units:
    hp = 0
    damage = 0
    speed = 0
    def minjae():
        pass

timo = Units()
timo.hp = 10
timo.damage = 100
timo.speed = 50

yasuo = Units()
yasuo.hp = 5
yasuo.damage = 1000
yasuo.speed = 100

print("티모 - 체력 : {0} | 공격력 : {1} | 이속 : {2}".format(timo.hp, timo.damage, timo.speed))



agent.move("forwad")
agent.place(1, "down")