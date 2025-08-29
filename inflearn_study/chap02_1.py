# print 사용법

print('Python Start')
print("double quote")
print('''python 
      triple''')
print("""python 
      triple 
      double""")


#seperator option

print('a', 'b', 'c', 'd', sep='')
print("010", '1234', '5678', sep='-')
print('python', 'google.com', sep='@')


# end option
print('Welcome to', end=' ')
print("IT news", end=' ')
print("Web Site")


# file option
import sys
print('Learn python', file = sys.stdout)



# formatting (decimal, string, floating point)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s 표처럼 그릴 수 있게
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))

print('{:^>10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('niceplayer'))

print('{:10.5}'.format('niceplayer'))


# %d
print("%d %d" % (1, 2))
print("{} {}".format(1, 2))

print("%-4d" % (421))
print("{:<4d}".format(42))



# %f

print('%f' % (3.15344332443))
print('{:f}'.format(3.11324134))

print('%06.2f' % (3.14325324))
print('{:06.2f}'.format(3.14325324))



# f-string

x = 50
y = 100
text = 308276567
n = 'lee'

ex1 = 'n = %s, s = %d, sum = %d' % (n, text, (x + y))
print(ex1)


ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)


ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)


# 구분기호
m = 1000000000
print(f'm : {m:,}')


# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20

print(f't : {t:10}')
print(f't center : {t:^10}')
print(f't center : {t:<10}')
print(f't center : {t:>10}')


print(f't center : {t:-^10}') # 기호로 빈칸 채우기
print(f't center : {t:|>10}')