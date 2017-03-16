"""
题目：算法导论6.5-9
思路：
1.把每个链表第一个元素加入到最小堆中
2.每次取出堆中最小的元素，并把该元素所在链表的下一个元素添加到堆中，并在该链表中删除该元素
（注意，使用链表的话就可以直接根据.next来判断下一个元素了，下面的方法没有用链表而是一个个判断，时间复杂度提高到了O(nk)）
3.重复1.2.直到所有元素都到位
"""
from min_heap import MinHeap


def merge_list(L):

    heap_list = []
    result_list = []

    for linklist in L:
        if linklist:
            heap_list.append(linklist[0])

    mheap = MinHeap(heap_list)
    mheap.build_heap()
    while len(mheap.A) > 1:
        elem = mheap.heap_extract_min()
        result_list.append(elem)
        for linklist in L:  # 因为没实现链表，所以要手动找出最小的是属于哪个数组...时间复杂度又变成O(nk)了
            if linklist and linklist[0] == elem:
                del linklist[0]
                if linklist:
                    mheap.min_heap_insertion(linklist[0])
                break

    return result_list


if __name__ == '__main__':
    L = [[1, 50, 70], [-5, 5], [60, 77, 81, 99], [100]]
    result = merge_list(L)
    for elem in result:
        print(elem)
