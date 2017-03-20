"""
最小堆与最小优先队列
"""


class MinHeap:

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
    def min_heapify(self, i):

        while i <= int(self.heap_size / 2):
            l = self.left(i)
            r = self.right(i)
            shortest = i
            if l and self.A[l] < self.A[shortest]:
                shortest = l
            if r and self.A[r] < self.A[shortest]:
                shortest = r
            if shortest != i:
                self.A[i], self.A[shortest] = self.A[shortest], self.A[i]
                i = shortest
            else:
                break  # 如果不加可能会有死循环

    # 建立堆
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
        if self.A[i] < key:
            print('新的关键词比原来大')
        self.A[i] = key
        while i > 1 and self.A[self.parent(i)] > key:
            self.A[i] = self.A[self.parent(i)]
            i = self.parent(i)
        self.A[i] = key

    def min_heap_insertion(self, key):
        self.heap_size += 1
        self.A.append(65535)
        self.heap_decrease_key(self.heap_size, key)


if __name__ == '__main__':

    pq = MinHeap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
    pq.build_heap()
    print('min:' + str(pq.heap_extract_min()))
    for num in pq.A[1:]:
        print(num)

    print('\n')
    pq.min_heap_insertion(10)
    print('Insertion:')
    for num in pq.A[1:]:
        print(num)


