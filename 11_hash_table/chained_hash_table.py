class Element:

    def __init__(self, key, info=None):
        self.key = key
        self.info = info
        self.next = None


class ChainedHashTable:

    def __init__(self, size):
        self.size = size  # 如果是表头元素这个的值就记录链表的长度
        self.T = [Element(0) for _ in range(self.size)]

    def h(self, x):
        pos = x.key % self.size
        return pos

    def chained_hash_insert(self, x):
        pos = self.h(x)
        self.T[pos].key += 1
        x.next = self.T[pos].next
        self.T[pos].next = x

    def chained_hash_search(self, x):
        pos = self.h(x)
        ptr = self.T[pos]
        while ptr.next:
            ptr = ptr.next
            if ptr == x:
                return ptr
        return None

    def chained_hash_delete(self, x):
        pos = self.h(x)
        ptr = self.T[pos]
        ptr.key -= 1
        while ptr.next and ptr.next != x:
            ptr = ptr.next
        ptr.next = ptr.next.next

if __name__ == '__main__':
    cht = ChainedHashTable(10)
    cht.chained_hash_insert(Element(10, 'patrick'))
    x = Element(20, 'cty')
    cht.chained_hash_insert(x)
    y = Element(18)
    cht.chained_hash_insert(y)
    cht.chained_hash_insert(Element(0))
    print(cht.chained_hash_search(x).info)
    cht.chained_hash_delete(y)
    print('end')
