class OpenAddressHashTable:

    def __init__(self, size=13, m=13, _m=11):
        self.size = size
        self.T = [None for _ in range(self.size)]
        self.m = m
        self._m = _m

    def h1(self, k):
        return k % self.m

    def h2(self, k):
        return 1 + k % self._m

    def h(self, k, i):
        return (self.h1(k) + i * self.h2(k)) % self.size

    def hash_insert(self, k):
        i = 0
        while i <= self.size:
            j = self.h(k, i)
            if self.T[j] is None:
                self.T[j] = k
                return j
            else:
                i += 1
        print('Overflow')
        return None

    def hash_search(self, k):
        i = 0
        j = self.h(k, i)
        while self.T[j] and i <= self.size:
            if self.T[j] == k:
                return j
            i += 1
            j = self.h(k, i)
        return None

    def hash_delete(self, k):
        pos = self.hash_search(k)
        if not pos:
            print('Element doesn\'t exist!')
            return
        self.T[pos] = None


if __name__ == '__main__':
    oaht = OpenAddressHashTable()
    oaht.hash_insert(79)
    oaht.hash_insert(69)
    oaht.hash_insert(72)
    oaht.hash_insert(98)
    oaht.hash_insert(14)
    print(oaht.hash_search(69))
    print(oaht.hash_search(14))
    oaht.hash_delete(14)
    print('end')
