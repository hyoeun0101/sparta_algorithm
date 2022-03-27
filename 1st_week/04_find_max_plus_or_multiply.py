input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result=array[0]
    for i in array[1:]: # N
        if i <= 1 or result <= 1: #2
            result+=i #2
        else:
            result*=i #2

    return result

# 시간 복잡도 O(N)

result = find_max_plus_or_multiply(input)
print(result)