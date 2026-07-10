drinks = {"콜라":[1000, 20, 0], "사이다":[1200, 20, 0], 
          "생수":[800, 20, 0], "커피":[1500, 20, 0]}

money = int(input("돈넣어라"))

for name, data in drinks.items():
    if money >= data[0]:
        print(f"{name} : {data[0]}원")

select = input("물건골라")
money -= drinks[select][0]
drinks[select][1] -= 1
drinks[select][2] += 1
print(f"{select} 드립니다. 잔액은 {money}원 입니다")
