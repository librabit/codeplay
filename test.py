class 참치선물세트():
    def __init__(self, 일반, 야채, 고추):
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추

    def 내용물보기(self, name):
        print(name)
        print("일반참치 : " + str(self.일반))
        print("야채참치 : " + str(self.야채))
        print("고추참치 : " + str(self.야채))  

class 특별선물세트(참치선물세트):
    def __init__(self, 일반, 스팸, 올리브유):
        super().__init__(일반, 0, 0) #상위클래스의 생성자(init)에서 3개의 변수 중 1개만 가져옴
        self.스팸 = 스팸 #특별선물세트에서만 쓰는 변수 만들기
        self.올리브유 = 올리브유 #특별선물세트에서만 쓰는 변수 만들기

특별01 = 특별선물세트(6, 3, 2)
특별01.내용물보기("특별세트 1호")