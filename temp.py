# # # name = ['���̾�','������', '������', '���ο�', '������']
# # # height = [170, 180, 160, 150, 140]

# # # for k in range(5):
# # #     print(f"ģ���̸� : {name[k]} / Ű : {height[k]}")

# # # max = max(height)
# # # max_idx = height.index(max)
# # # small = min(height)
# # # small_idx = height.index(small)
# # # avr = sum(height) / len(height)
# # # low = []
# # # high = []

# # # high.append()

# # # print("���Ű :", avr)

# # # name[height.index(Ű)]

# # # print(f"Ű ��ū�� : {name[max_idx]} / {max} \nŰ �������� : {name[small_idx]} / {small}")

# # # # ȭ�鿡 �Ʒ��� ���� ����Ͻÿ�
# # # '''
# # # ���� Ű ū ģ�� : �̸� / Ű
# # # ���� Ű ���� ģ�� : �̸� / Ű
# # # ��պ��� ���� �༮�� : �̸��� (�̸�)
# # # ��պ��� ũ�ų� ���� �༮�� : �̸��� (�̻�)
# # # '''
# # # for o in range(len(height)):
# # #     if height[o] < avr:
# # #         pass
# # #     else:
# # #         pass


# # # �����ֽļ� = '5,343,323'
# # # �����ֽļ�2 = int(�����ֽļ�.replace(',', ''))
# # # print(�����ֽļ�2, type(�����ֽļ�2))

# # # name1 = "��μ�" 
# # # age1 = 10
# # # name2 = "��ö��"
# # # age2 = 13

# # # print(f'�̸� : {name1}  ���� : {age1}')
# # # print(f'�̸� : {name2}  ���� : {age2}')

# # # �б� = "2020/03(E) (IFRS����)"
# # # print(�б�[:7])
# # # data = "   �Ｚ����    "
# # # print(data.strip())
# # # # ticker.upper()
# # # ticker = "btc_krw"
# # # t = ticker.split('_')
# # # print(t)
# # # date = "��������ؿ�ٺ�"
# # # d = date.split('���ؿ�')
# # # print(d)

# # movie = ['��Ʈ��', '��Ʈ��', '�¹��']
# # star = ['�ڵ���', '���ؿ�', '�鿵��']
# # movie.append("��Ʈ��")
# # movie.insert(1, '�����̴���')
# # # del movie[3]
# # # movie.remove("������")
# # print(movie)
# # names = movie + star
# # print(names)

# # nums = [1, 2, 3, 4, 5, 6, 7]
# # print(min(nums))
# # print(max(nums))
# # print(sum(nums))
# # print(len(nums))
# # print(sum(nums)/len(nums))
# # # all = 0
# # # for i in nums:
# # #     all += i
# # # print(all)



# # num = input("���� : ")

# # if num.islower():
# #     print(num.upper())
# # else:
# #     print(num.lower())


# # def max(a,b):
# #     if a>b:
# #         return a
# #     else:
# #         return b
# # a, b, c = input(""), input(), input()
# # print(max(a, max(b, c)))

# # 10������ ��ٷ� 2������ �ٲٱ�.
# # 10���� 5 -> 2���� 101
# # 10���� 24 -> 2���� 11000

# def two(ten): #5
#     answer = ""
#     if ten > 0:
#         while ten:
#             answer += str(ten % 2)
#             ten //= 2
#         return int(answer[::-1])
#     else:
#         return ten
# print(two(132))

# t = input("������ �����ÿ�: ")
# print(t, eval(t))

# a = input("����")

# if int(a) % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# 1. �Լ��� ����
a = 0
def calc1(a, b):
    result = a + b # calc�ȿ����� ���� ��������
    return result

def calc2(a, b):
    result = a - b
    return result

# 2. �Լ� ȣ��

while True:
    c = input("���ϴ� ��� 1.���� 2.���� 9.������")
    n1 = int(input("����1 : "))
    n2 = int(input("����2 : "))
    if c == "9":
        print("���� ����")
        break
    elif c == "1":
        a = calc1(n1, n2)
    elif c == "2":
        a = calc2(n1, n2)
    print("����� : ", a)
