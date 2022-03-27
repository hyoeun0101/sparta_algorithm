class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)

    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next != None:#노드 끝까지 이동.
            cur = cur.next
        cur.next = Node(value) # 노드 끝까지 이동 후 노드 추가

    def print_all(self):
        cur = self.head
        while cur.next != None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

# node= Node(3)
# print(node.data)


# first_node =Node(5)
# second_node=Node(12)
# first_node.next = second_node

liked_list = LinkedList(5)
liked_list.append(12)
liked_list.append(8)
liked_list.print_all()