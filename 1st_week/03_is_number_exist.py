input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:#N
        if element == number:# 1
            return True
    return False

#시간 복잡도 : N
# 최선의 상황 - 찾으려는 값이 array 맨 앞에 있으면 시간 복잡도 : 1
# 최악의 상황 - 찾으려는 값이 array 맨 뒤에 있으면 시간 복잡도 : N
# 빅오: N
# 빅오메가 : 1

result = is_number_exist(3, input)
print(result)