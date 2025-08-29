# from function import sachik



# sachik()



def func_a(arr):
	        #  0, 1, 2, 3, 4 인덱스 번호
	counter = [1, 5, 1, 0, 1]
	arr = [1, 2, 1, 3, 1, 1, 3, 1, 0]
	for x in arr:
		counter[x] += 1
	return counter