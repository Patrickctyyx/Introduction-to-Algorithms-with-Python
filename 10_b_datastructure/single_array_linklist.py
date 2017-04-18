"""
对象的单数组表示法
L 为表头元素，指向链表的第一个元素
free 为空链表的表头元素
array 连续三个元素表示链表的一个节点，位置 x 就相当于指针
这里实现了对象的分配和释放操作，插入和删除没有实现
"""


class SingleArrayLinkList:

    def __init__(self, size):

        self.L = None
        self.free = 0
        self.array = [None for i in range(3 * size)]
        i = 1
        for num in range(size - 1):
            self.array[i] = i + 2
            i += 3

    def allocate(self):
        if self.free is None:
            print('Out of Space')
            return None
        x = self.free
        self.free = self.array[x + 1]
        return x

    def free(self, x):
        self.array[x + 1] = self.free
        self.free = x
