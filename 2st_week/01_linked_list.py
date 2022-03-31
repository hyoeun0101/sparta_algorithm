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
        while cur != None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        print(node)
        return node

    def add_node(self, index, value):
        # cur = self.head
        # for _ in range(index):
        #     cur = cur.next
        new_node = Node(value)
        if index==0:
            new_node.next = self.head
            self.head = new_node

        node = self.get_node(index-1)
        new_node.next = node.next
        node.next = new_node
    
    def delete_node(self, index):
        if index == 0:
            node = self.head
            self.head = node.next
        node= self.get_node(index-1)
        node.next =node.next.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(4)

linked_list.add_node(2, 3)#index번째에 value추가
linked_list.delete_node(2)
linked_list.print_all()