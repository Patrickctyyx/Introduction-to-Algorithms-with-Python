"""
桶排序
思路：将n个输入数放入桶（n个大小相同的子区间）中，再对桶中的每个元素进行排序，输出就只用遍历每个桶
稳定性：稳定
时间复杂度：平均为O(n)，最差为O(n^2)
"""

from linklist import *


def bucket_sort(A):
    n = len(A)
    B = [Node(None) for i in range(n)]
    for elem in A:
        temp = Node(elem)
        prev = B[int(n * elem)]
        ptr = prev.next
        # 把元素插入到链表中，直接就是插入排序了
        while ptr:
            if ptr.elem <= elem:
                prev = ptr
                ptr = ptr.next
            elif ptr.elem > elem:
                break
        temp.next = prev.next
        prev.next = temp

    return B

if __name__ == '__main__':
    A = [0.79, 0.13, 0.16, 0.24, 0.39, 0.20, 0.29, 0.23, 0.71, 0.42]
    C = bucket_sort(A)




