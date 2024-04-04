def solution(sides):
    answer = 0
    top = sides.pop(max(sides))
    two = sum(sides)
    print(top, two)
    if top < two:
        answer = 1
    else:
        answer = 2
    return answer

arr1 = [1, 2, 3]
arr2 = [8, 10, 9]
arr3 = [199, 72, 222]
solution(arr1)
solution(arr2)
solution(arr3)