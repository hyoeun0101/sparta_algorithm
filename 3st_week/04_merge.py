array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array3=[]
    idx1=0
    idx2=0
    while idx1<len(array1) and idx2<len(array2):
        if array1[idx1] < array2[idx2]:
            array3.append(array1[idx1])
            idx1+=1
        else:
            array3.append(array2[idx2])
            idx2+=1 
    if idx1 == len(array1):
        array3.extend(array2[idx2:])
    else:
        array3.extend(array1[idx1:])
    return array3


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
