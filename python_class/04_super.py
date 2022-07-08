class Unit:
    def __init__(self):
        print("일반유닛 속성")

class Air:
    def __init__(self):
        print("공중유닛 속성")

class AirUnit(Air, Unit):
    def __init__(self):
        # super().__init__() #다중상속시 순서에 영향을 받기때문에 다중상속에서 super는 안씀.
        Unit.__init__(self)
        Air.__init__(self)

dropship = AirUnit()