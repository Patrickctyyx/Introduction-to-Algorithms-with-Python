"""
计数排序
思想：找到数组中值为A[i]的元素所在的位置，并且把它放在数组B中
时间复杂度:O(n)
稳定性：稳定
缺点：占用空间比较大，如果数组中最大值和最小值相差很大，而且要求最小值不能小于0
"""


def counting_sort(A, k):
    B = [None for b in range(len(A))]
    C = [0 for i in range(k + 1)]
    for elem in A:
        C[elem] += 1
    for i in range(k):
        C[i + 1] += C[i]

    for i in range(len(A)):
        temp = A[-(i + 1)]
        B[C[temp] - 1] = temp
        C[temp] -= 1
    return B

if __name__ == '__main__':
    result = counting_sort([6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2], 6)
    for num in result:
        print(num)
