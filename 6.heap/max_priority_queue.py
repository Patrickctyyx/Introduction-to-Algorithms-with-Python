"""最大优先队列"""

from heap_sort import HeapSort


class MaxPriorityQueue:

    def __init__(self, A):

        self.aheap = HeapSort(A)

    def heap_max(self):
        return self.aheap.A[1]

    def heap_extract_max(self):
        if self.aheap.heap_size < 1:
            print('此时不允许去掉元素')
        max_elem = self.aheap.A[1]
        self.aheap.A[1] = self.aheap.A[self.aheap.heap_size]
        self.aheap.A.pop()
        self.aheap.heap_size -= 1
        self.aheap.max_heapify(1)
        return max_elem

    def heap_increase_key(self, i, key):
        if self.aheap.A[i] > key:
            print('新的关键字比原来更小')
        self.aheap.A[i] = key
        while i > 1 and self.aheap.A[self.aheap.parent(i)] < key:  # 注意第二个条件应该每次都是和key比较
            self.aheap.A[i] = self.aheap.A[self.aheap.parent(i)]
            i = self.aheap.parent(i)
        self.aheap.A[i] = key

    def max_heap_insertion(self, key):
        self.aheap.heap_size += 1
        self.aheap.A.append(-65536)
        self.heap_increase_key(self.aheap.heap_size, key)


if __name__ == '__main__':

    pq = MaxPriorityQueue([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
    print('max: ' + str(pq.heap_extract_max()))
    for num in pq.aheap.A[1:]:
        print(num)
    print('\n')
    pq.max_heap_insertion(10)
    print('Insertion:')
    for num in pq.aheap.A[1:]:
        print(num)

