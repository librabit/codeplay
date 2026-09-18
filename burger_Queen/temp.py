start, end = int(input("시작단")), int(input("끝단"))

for dan in range(start, end + 1):
    print(dan, "단 시작", "=" *10)
    for gopsu in range(1, 20): 
        print(dan, "x", gopsu, "=" , dan * gopsu)

