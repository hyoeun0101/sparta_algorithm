# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    count=0
    for number in array:
        count+=1
        if target == number:
            print(count)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True

# 시간 복잡도 : O(N)