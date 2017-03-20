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
    return i + 1


def qsort(L, p, r):
    if p < r:
        q = partition(L, p, r)
        qsort(L, p, q - 1)
        qsort(L, q + 1, r)


if __name__ == '__main__':
    l = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    qsort(l, 0, 11)
    for m in l:
        print(m)
