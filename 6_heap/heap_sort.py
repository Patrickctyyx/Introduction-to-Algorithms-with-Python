"""最大堆以及堆排序"""


class HeapSort:

    def __init__(self, A):
        self.heap_size = len(A)
        self.A = A
        self.A.insert(0, 0)  # 从第二个元素开始才是，也就是说A[1]开始

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

    # 维护堆
    def max_heapify(self, i):

        while i <= int(self.heap_size / 2):
            l = self.left(i)
            r = self.right(i)
            longest = i
            if l and self.A[l] > self.A[longest]:
                longest = l
            if r and self.A[r] > self.A[longest]:
                longest = r
            if longest != i:
                self.A[i], self.A[longest] = self.A[longest], self.A[i]
                i = longest
            else:
                break  # 如果不加可能会有死循环

    # 建立堆
    def build_heap(self):

        i = int(self.heap_size / 2)
        while i:
            self.max_heapify(i)
            i -= 1

    # 堆排序
    def heap_sort(self):

        self.build_heap()
        i = self.heap_size
        while i > 1:
            self.A[1], self.A[i] = self.A[i], self.A[1]
            self.heap_size -= 1
            self.max_heapify(1)
            i -= 1


if __name__ == '__main__':
    # 测试
    aheap = HeapSort([5, 3, 17, 10, 84, 19, 6, 22, 9])
    aheap.heap_sort()
    for num in aheap.A[1:]:
        print(num)
