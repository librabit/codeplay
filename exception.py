a = [1, 2, 3, 4, 5]

count = 0
running = True
while running:
    try:
        for i in range(len(a)+1):
            print(a[i])
    except IndexError:
        print("인덱스가 모자라네요")

    print("코드는 계속된다")
    count += 1

    if count > 10:
        running = False