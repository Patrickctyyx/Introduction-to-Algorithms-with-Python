"""
期望为线性时间的选择算法：
思想：根据快速排序的划分方法把数组划成两部分，但是如果没找到就只在选择i所在的那一部分继续进行划分
"""

from random import randint


def partition(L, p, r):

    ran = randint(p, r)
    L[r], L[ran] = L[ran], L[r]
    pivot = L[r]
    i = p - 1
    for j in range(p, r):  # 生成p到r - 1的数
        if L[j] <= pivot:
            i += 1
            L[j], L[i] = L[i], L[j]
    L[i + 1], L[r] = L[r], L[i + 1]
    return i + 1  # 返回 pivot


# 寻找第i小的元素
def select(L, p, r, i):
    if p == r:
        return L[p]
    q = partition(L, p, r)
    k = q - p + 1
    if k == i:
        return L[q]
    elif k < i:
        # 在新的数组里面原来的第i小的现在是第i - k小了，因为开头的元素改变了
        return select(L, q + 1, r, i - k)
    # 而在这里相对位置不变，因为开头的元素没有变化
    return select(L, p, q - 1, i)

if __name__ == '__main__':
    L = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(select(L, 0, 8, 5))

