# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # binary search
    # 시간복잡도 : O(M*logN) , orders의 개수 : M, menus의 길이 : N
    menus.sort()
    for order in orders:
        if not binary_search(order, menus):
            return False
    return True

    # set사용
    # 리스트 in연산자 사용 : O(N)
    # set, dict in연산자 사용 : O(1), 최악- O(N)
    # 따라서 set으로 바꾼 후 in연산을 하는게 좋음
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set: # menus_set.__contains__(order)
            return False
    return True


def binary_search(target, array):
    first=0
    last=len(array)-1
    while first <= last:
        mid = (first+last)//2
        if target == array[mid]:
            return True
        elif target < array[mid]:
            last = mid-1
        else:
            first = mid+1
    
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)