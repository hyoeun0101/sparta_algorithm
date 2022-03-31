# 이진탐색 -> 오름차순으로 정렬되어 있어야함.
# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    
    first = 0
    last = len(array)-1
    count=0
    while first < last:
        mid=(first+last)//2
        count+=1
        if target > array[mid]:
            first = mid+1
        elif target < array[mid]:
            last = mid-1
        else:
            print(count)
            return mid
        
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

#시간 복잡도 : O(logN)
# 총 숫자가 1~N까지라고 한다면,
# k번 탐색하면 N/2^k 가 남는다.
# N/2^k = 1
# k = log N