# 기본 선언

n = 700


# 동시 선언

x = y = z = 700
print(x, y, z)


# object reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300))

# ex2)
n = 777

print(n, type(n))

m = n # m -> 777 <- n

print(type(m), type(n))

m = 400

print(m, n)