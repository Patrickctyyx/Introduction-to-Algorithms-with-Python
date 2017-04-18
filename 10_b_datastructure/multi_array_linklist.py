"""
对象的多数组表示法
L 为表头元素，指向链表的第一个元素
free 为空链表的表头元素
next，key，prev 三个数组同一个位置的元素表示链表的一个节点，位置 x 就相当于指针
这里实现了对象的分配和释放操作，插入和删除没有实现
"""


class MultiArrayLinkList:

    def __init__(self, size):
        self.free = 0
        self.L = None
        self.next = [i + 1 for i in range(size - 1)]
        self.next[size - 1] = None
        self.key = [None for i in range(size)]
        self.prev = [None for i in range(size)]

    def allocate(self):  # 插入元素之前使用
        if self.free is None:
            print('Out of Space!')
            return None
        x = self.free
        self.free = self.next[x]
        return x

    def free(self, x):  # 删除元素之后使用
        self.next[x] = self.free
        self.free = x
