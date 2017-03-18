class Node:

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LinkList:

    def __init__(self, _list):
        self.length = len(_list)
        self.head = Node(0)
        for i in range(self.length):
            j = self.length - i - 1
            temp = Node(_list[j])
            temp.next = self.head.next
            self.head.next = temp

    def extractFirst(self):
        temp = self.head.next
        self.head.next = temp.next
        return temp


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = LinkList(l)
    node = ll.head
    while node.next:
        print(node.next.elem)
        node = node.next
