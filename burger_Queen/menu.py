
class MenuItem():
    def __init__(self, name, price, cook_time):
        self.name = name
        self.price = price
        self.cook_time = cook_time

class Burger(MenuItem):
    def __init__(self, name, price, patty, patty_q, cook_time, bread="참깨빵"):
        self.estimate = (cook_time * patty_q) + 60
        super().__init__(name, price, cook_time)

        self.patty = patty
        self.patty_q = patty_q
        self.bread = bread
        self.basic = ['양파', '양상추', '토마토', '피클']
        self.sold_out = False

class SpecialBurger(Burger):
    def __init__(self, name, price, patty, patty_q, cook_time, special):
        super().__init__(name, price,patty, patty_q, cook_time, bread = "브리오슈번")
        self.special = special

class Side(MenuItem):
    def __init__(self, name, price, cook_time):
        super().__init__(name, price, cook_time)


class Drinks(MenuItem):
    def __init__(self, name, price, cook_time=30):
        super().__init__(name, price, cook_time)

class SetMenu():
    def __init__(self, burgers, sides, drinks):
        self.burgers = burgers
        self.sides = sides
        self.drinks = drinks
        self.name = burgers.name + " 세트"

        total_price = burgers.price + sides.price + drinks.price

        self.discount = int(total_price * 0.8)

# 일반버거
b1 = Burger('치즈버거', 5000, "쇠고기+치즈", 1, 120)
b2 = Burger('오징어짬뽕버거', 9000, "오징어다리", 1, 120)
b3 = Burger('용문산나물버거', 15000, "산나물10종", 1, 120)

# 스페셜버거
sb1 = SpecialBurger("오예스폭탄버거", 15000, "오예스말고기볶음", 5, 6000, "시골청국장소스")
sb2 = SpecialBurger("맥도날드빅맥", 25000, "쇠고기패티", 2, 106000, "랜치소스")

# 사이드 메뉴
s1 = Side('소세지야채볶음', 3000, 120)
s2 = Side('감자튀김', 3000, 120)
s3 = Side('소머리국밥', 9000, 1200)

# 음료
d1 = Drinks("매실차", 5000)
d2 = Drinks("막걸리", 8000)
d3 = Drinks("약숫물", 2000)
d4 = Drinks("초정사이다", 7000)

# 세트메뉴
set1 = SetMenu(b1, s1, d1)
set2 = SetMenu(b2, s1, d1)
set3 = SetMenu(b3, s1, d1)
set4 = SetMenu(sb1, s1, d1)
set5 = SetMenu(sb2, s1, d1)


