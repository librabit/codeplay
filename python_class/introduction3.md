모듈화# 모듈과 패키지

잘 짜여진 코드는 쓰고 또 써도 쓸때마다 이득.  
그래서 필요한 것이, 유용한 코드를 클래스/함수화 하고, 이 코드를 별도의 파일로 만들어두는 모듈화/패키지화가 필요하다.  

## 1. 모듈화
앞서 수업에서 실습문제로 만든 LoL char 클래스 코드를 떠올려 보자.

    class char():
        def __init__(self, hp, attack, speed):
            self.hp = hp
            self.atk = atk
            self.speed = speed
        def stat(self, name):
            print(name)
            print(f"hp : {self.hp}")
            print(f"atk : {self.atk}")
            print(f"speed : {self.speed}")

    class champ(char):
        def __init__(self, hp, atk, speed, q, w, e, r):
            super().__init__(hp, atk, speed)
            self.q = q
            self.w = w
            self.e = e
            self.r = r  
        def stat(self, name):
            super().stat(name)
            print(f"Q_skill : {self.q}")
            print(f"W_skill : {self.w}")
            print(f"E_skill : {self.e}")        
            print(f"R_skill : {self.r}")    

    미니언01 = char(100, 5, 20)
    미니언01.stat("미니언1번의 상태")
    야스오 = champ(100, 1000, 500, "찌르기", "장막", "돌진", "난도질") 
    야스오.stat("야스오의 상태")

위의 코드에서 char들은 블루진영과 레드진영 양측에서 등장해야 한다.  
그럴때, 위의 클래스를 양쪽 진영에서 모두 동일한 코드를 사용해야 한다면, 모듈로 만들어두고 진영별로 각자 가져다 쓸 수 있을것이다.

그렇다면 어떻게 모듈을 만들까?

### 1. 클래스 파일만 따로 모아 파일로 만들기
위의 예제에서 클래스 선언부분만 따로 파일로 저장한다.

    # character_class.py로 아래 내용 저장
    class char():
        def __init__(self, hp, atk, speed):
            self.hp = hp
            self.atk = atk
            self.speed = speed

        def stat(self, name):
            print(name)
            print("hp : {}".format(self.hp))
            print("atk : {}".format(self.atk))
            print("speed : {}".format(self.speed))

    class champ(char):
        def __init__(self, hp, atk, speed, q, w, e, r):
            super().__init__(hp, atk, speed)
            self.q = q
            self.w = w
            self.e = e
            self.r = r
    
        def stat(self, name):
            super().stat(name)
            print("Q_skill : {}".format(self.q))
            print("W_skill : {}".format(self.w))
            print("E_skill : {}".format(self.e))        
            print("R_skill : {}".format(self.r)) 

### 2. 진영별 파일을 만들고, 모듈을 불러와 객체 생성

    # blue_team.py 파일을 만들고 저장
    import character_class

    미니언01 = character_class.char(100, 5, 20)
    미니언01.stat("미니언1번의 상태")
    야스오 = character_class.champ(100, 1000, 500, "찌르기", "장막", "돌진", "난도질") 
    야스오.stat("야스오의 상태")

    # red_team.py 파일을 만들고 저장
    import character_class

    미니언01 = character_class.char(100, 5, 20)
    미니언01.stat("미니언1번의 상태")
    티모 = character_class.champ(10, 10000, 5000, "실명다트", "speed증가", "맹독다트", "버섯함정") 
    티모.stat("티모의 상태")

앞서 만든 character_class.py 파일은 2개의 클래스가 정의된 파일이다.  
이 파일을 다른 파일이 가져다 쓰기 위해서는(모듈사용) 3가지 규칙이 필요하다.
> 
> 1. 모듈 파일이 사용하고자 하는 파일과 경로상 같은 곳에 있을 것 (같은 폴더내에 존재할 것)
> 2. 불러오는 파일의 맨 윗줄에 import 명령어로 파일명을 .py를 제외하고 적어줄 것 (해당 파일을 모듈로 쓰기위해 가지고 들어오겠다는 의미)
> 3. 모듈을 사용할 때에는 모듈명 뒤에 점을 찍고 클래스명을 적어 적용할 것 (미니언01 = character_class.char(100, 5, 20) => **미니언01**이라는 인스턴스를 **character_class 라는 모듈** 안에 있는 **char라는 클래스**를 이용해 생성하겠다는 의미)  

이렇게 특별한 기능의 코드를 별도의 파일로 저장하고, 필요할 때 불러다 쓰는 방법을 **"모듈화"**라고 부르며, 각각의 파일은 모듈이라 부른다.

모듈 안에는 **클래스** 뿐만 아니라 **함수**와 **변수**도 사용이 가능하다.

## 2. 모듈 편하게 쓰기
### 모듈에 별명붙여 짧게 쓰기
위에서 만든 모듈 **character_class**라는 모듈명은 계속해서 쓰기엔 길이가 길어 코드를 치기 귀찮기도 하고 가독성도 떨어진다.  
이럴 때 모듈명을 짧게 별명으로 불러올 수도 있다.

    import character_class as cs

    미니언01 = cs.char(100, 5, 20)

위처럼 **as**를 붙이고 원하는 이름을 적으면 그 별명으로 클래스를 사용할 수 있다.

> import ** as ? => **을 가져오되, ?으로 부르자 라는 의미

### 모듈 안의 클래스, 함수, 변수 바로 가져다 쓰기
모듈을 불러오고, 그 안의 함수를 쓰는 방법은 별명이든 본명이든 불러온 모듈명을 적어주고 사용을 해야하는 단점이 있다.  
모듈 내부의 클래스, 함수, 변수 이름을 알고 있다면 해당 클래스, 함수, 변수를 바로 가져와 쓸 수 있다.

    from character_class import char, champ

    미니언01 = char(100, 5, 20)
    미니언01.stat("미니언1번의 상태")
    야스오 = champ(100, 1000, 500, "찌르기", "장막", "돌진", "난도질") 
    야스오.stat("야스오의 상태")

위의 예제에서 import 뒤에 적힌 2개의 클래스명은 불러온 파일 안에서 직접 선언한 클래스인 것으로 간주된다.  
그래서 모듈명을 따로 쓰지 않고 직접 사용이 가능하다.

특정한 클래스, 함수, 변수를 적지 않고 전부 다 가져올 수도 있다.

    from character_class import *

위의 예제처럼 __*__ (별표 asterisk)를 사용하면 **character_class.py** 파일 안에 있는 모든 클래스, 함수, 변수를 모두 긁어오게 된다.

이때 주의할 점이 있다. 모든 내용물을 긁어오는 것이기 때문에 사용하는 파일에서 선언하는 클래스, 함수, 변수(특히 변수)와 이름이 겹칠 경우 오류가 발생할 수 있기 때문이다.  

그렇기 때문에 모든 내용물을 긁어오기 보다는 필요한 것들만 불러다 쓰는 것이 좋다.  
상단의 import 옆에 씌여진 기능의 이름이 상단에 보이기 때문에 중복되는 이름으로 객체를 생성하는 실수를 방지할 수도 있다.

## 3. 모듈의 묶음, 패키지 package
이렇게 편리한 모듈이지만, 대규모 프로젝트를 하고 있다면 모듈이 수십 수백개를 만들어야 하는 상황이 생긴다. 이럴 때 복잡하지 않게 폴더를 만들어 정리를 해두는 방법이 바로 **패키지 package** 이다. 

앞서 만든 character_class.py 파일을 sprite라는 폴더를 만들어 옮겨두자.   
그리고 모듈을 불러올 파일에서 아래와 같이 적으면 된다.

    import sprite.character_class as cs

**폴더명.모듈파일명**의 구조를 통해 폴더내의 파일에 접근할 수 있다. 
위의 방법의 경우 **as**를 통해 별명을 짓지 않으면 어마어마하게 패키지명이 길어지기 때문에 대부분 짧게 줄여서 불러쓰게 된다.

# 4. 마치며 : 파이썬은 모든게 객체!

파이썬의 내장함수(기본으로 제공하는 함수)중 **type()**이라는 함수가 있다. 
마찬가지로 내장함수인 **print()**와 함께 사용해 몇 가지 변수를 만들고 확인해 볼 것이 있다.

    texts = "텍스트"
    numbers = 1234
    lists = []
    tuple = ()

    print(type(texts))
    print(type(numbers))
    print(type(lists))
    print(type(tuple))

라고 적어서 출력해 보면 아래와 같은 결과를 얻게 된다.

    <class 'str'>
    <class 'int'>
    <class 'list'>
    <class 'tuple'>

우리가 앞선 수업들에서 점을 찍고 무언가 기능을 사용했던 기억이 떠오르는가?

    lists.append("abc")

위의 예제에서 .append()는 리스트라는 클래스 안에 정의된 함수 중 하나이다. 리스트가 클래스이기 때문에 해당 클래스 안에 정의된 매서드(함수), 변수 등을 가져다가 마음껏 활용할 수 있는 것이다.