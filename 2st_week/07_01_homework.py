# Q1 링크드 리스트의 끝에서 K번째 값 반환
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # # 1. 전체 길이 - k번째
        cur = self.head
        cnt=0
        while cur is not None:
            cnt+=1
            cur = cur.next
        cur = self.head
        for i in range(cnt-k):
            cur = cur.next
        return cur

        # 2. k만큼 떨어진 포인터 두개
        slow = self.head
        fast = self.head

        for _ in range(k):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow

# 시간 복잡도 : O(N)
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)


print(linked_list.get_kth_node_from_last(6).data)  # 7이 나와야 합니다!