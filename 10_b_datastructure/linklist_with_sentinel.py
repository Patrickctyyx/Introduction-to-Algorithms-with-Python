"""使用哨兵的链表，减少了对表第一个元素和表尾元素的判断"""


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self, _list):
        self.length = len(_list)
        self.nil = Node(0)
        self.nil.prev = self.nil
        self.nil.next = self.nil
        for i in range(self.length):
            j = self.length - i - 1  # 从后往前插入
            temp = Node(_list[j])
            temp.next = self.nil.next
            temp.prev = self.nil
            prev_node = self.nil.next
            prev_node.prev = temp
            self.nil.next = temp

    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.elem != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.nil.next
        x.prev = self.nil
        self.nil.next.prev = x
        self.nil.next = x

    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev


if __name__ == '__main__':
    A = [8, 7, 3, 9]
    ll = LinkList(A)
    n = ll.search(3)
    x = Node(4)
    ll.insert(x)
    ll.delete(n)
