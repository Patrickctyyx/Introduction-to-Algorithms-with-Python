"""
merge_list用链表实现，时间复杂度仍保持了O(nlg(k))
在传递node的时候一定要报称传递的是原来的node而不是新建的，这样才能保持“指针”不断裂
"""


from linklist import Node, LinkList


class LinkMinHeap:

    def __init__(self, A):
        self.heap_size = len(A)
        self.A = A
        self.A.insert(0, Node(0))

    def left(self, i):
        if 2 * i <= self.heap_size:
            return 2 * i
        return None

    def right(self, i):
        if 2 * i + 1 <= self.heap_size:
            return 2 * i + 1
        return None

    def parent(self, i):
        return int(i / 2)

    def min_heapify(self, i):

        while i <= int(self.heap_size / 2):
            l = self.left(i)
            r = self.right(i)
            shortest = i
            if l and self.A[l].elem < self.A[shortest].elem:
                shortest = l
            if r and self.A[r].elem < self.A[shortest].elem:
                shortest = r
            if shortest != i:
                self.A[i], self.A[shortest] = self.A[shortest], self.A[i]
                i = shortest
            else:
                break

    def build_heap(self):

        i = int(self.heap_size / 2)
        while i:
            self.min_heapify(i)
            i -= 1

    def heap_min(self):
        return self.A[1]

    def heap_extract_min(self):
        if self.heap_size < 1:
            print('此时不允许去掉元素')
        min_elem = self.heap_min()
        self.A[1] = self.A[self.heap_size]
        self.A.pop()
        self.heap_size -= 1
        self.min_heapify(1)
        return min_elem

    def heap_decrease_key(self, i, key):
        if self.A[i].elem < key:
            print('新的关键词比原来大')
        self.A[i].elem = key
        temp = self.A[i]
        while i > 1 and self.A[self.parent(i)].elem > key:
            self.A[i] = self.A[self.parent(i)]
            i = self.parent(i)
        self.A[i] = temp

    def min_heap_insertion(self, node):
        self.heap_size += 1
        key = node.elem
        node.elem = 65535
        self.A.append(node)  # 怪不得一直到第二个就不能继续了，原来这里的Node是新产生的
        # 应该直接把原来的Node传递过去！！！
        self.heap_decrease_key(self.heap_size, key)


def merge_list(L):

    heap_list = []
    result_list = []

    for i in range(len(L)):
        if L[i]:
            L[i] = LinkList(L[i])
            heap_list.append(L[i].head.next)

    mheap = LinkMinHeap(heap_list)
    mheap.build_heap()
    while len(mheap.A) > 1:
        elem = mheap.heap_extract_min()
        result_list.append(elem)
        if elem.next:
            mheap.min_heap_insertion(elem.next)

    return result_list


if __name__ == '__main__':
    L = [[1, 50, 70], [-5, 5, 6], [60, 77, 81, 99], [100]]
    result = merge_list(L)
    for elem in result:
        print(elem.elem)
