class Node:

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class LinkList:

    def __init__(self, _list):
        self.length = len(_list)
        self.head = Node(0)
        for i in range(self.length):
            j = self.length - i - 1  # 从后往前插入
            temp = Node(_list[j])
            temp.next = self.head.next
            temp.prev = None
            prev_node = self.head.next
            if prev_node:
                prev_node.prev = temp
            self.head.next = temp

    def search(self, k):
        x = self.head.next
        while x and x.elem != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head.next
        if x.next:
            x.next.prev = x
            self.head.next = x

    def delete(self, x):
        if x.prev:
            x.prev.next = x.next
        else:
            self.head.next = x.next
        if x.next:
            x.next.prev = x.prev


if __name__ == '__main__':
    A = [8, 7, 3, 9]
    ll = LinkList(A)
    n = ll.search(3)
    x = Node(4)
    ll.insert(x)
    ll.delete(n)



