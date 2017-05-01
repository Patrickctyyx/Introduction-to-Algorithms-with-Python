"""
完全散列：
采用两级散列，每级都是用全域散列
其中第二级散列的大小是元素个数的平方（为了防止冲突）
P.S. 感觉初始化真的好麻烦，散列函数的参数都是要根据特定的序列来进行指定
"""


class SecondaryHashTable:

    def __init__(self, m, a, b, p):
        # m 是元素个数的平方
        self.m = m
        # a 和 b 都是 hash 函数的项
        # h(k) = ((ak + b) mod p) mod m
        self.a = a
        self.b = b
        self.p = p
        self.table = [None for _ in range(self.m)]

    def h(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


class PerfectHashTable:

    def __init__(self, size, a, b, p):
        self.m = size
        self.a = a
        self.b = b
        self.p = p
        self.T = [None for _ in range(self.m)]

    def h(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

if __name__ == '__main__':
    pht = PerfectHashTable(9, 3, 42, 101)
    k = [10, 22, 37, 40, 52, 60, 70, 72, 75]
    pht.T[0] = SecondaryHashTable(1, 0, 0, 101)
    pht.T[2] = SecondaryHashTable(9, 10, 18, 101)
    pht.T[5] = SecondaryHashTable(1, 0, 0, 101)
    pht.T[7] = SecondaryHashTable(16, 23, 88, 101)
    for i in k:
        sht = pht.T[pht.h(i)]
        sht.table[sht.h(i)] = i
    print('end')
