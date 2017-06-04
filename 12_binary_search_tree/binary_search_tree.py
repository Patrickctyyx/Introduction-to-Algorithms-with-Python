"""
node.left.key > node > node.right.key

"""


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None


class BinarySearchTree:

    def __init__(self, T):
        # for i in range(1, T[0] + 1):
        #     if i > 1 and T[i]:
        #         T[i].p = T[int(i / 2)]
        #     if 2 * i <= T[0] and T[i]:
        #         T[i].left = T[2 * i]
        #     if 2 * i + 1 <= T[0] and T[i]:
        #         T[i].right = T[2 * i + 1]
        # root is T[1]
        # T[0] is the num of elements
        # 使用 tree_insert 来构建二叉搜索树
        self.tree = [0]
        for i in T:
            self.tree_insert(i)

    def inorder_tree_walk(self, root):
        if root:
            self.inorder_tree_walk(root.left)
            print(root.key)
            self.inorder_tree_walk(root.right)

    # 递归查找
    def tree_search(self, root, k):
        if root is None:
            print('Not found')
            return
        if root.key == k:
            print('found: ', root.key)
            return root
        if k > root.key:
            return self.tree_search(root.left, k)
        else:
            return self.tree_search(root.right, k)

    # 迭代查找
    def interactive_tree_search(self, root, k):
        while root and root.key != k:
            if k > root.key:
                root = root.left
            else:
                root = root.right
        if root:
            print('Found: ', root.key)
            return root
        else:
            print('Not found')
            return

    def tree_maximum(self, root):
        while root.left:
            root = root.left
        return root

    def tree_minimum(self, root):
        while root.right:
            root = root.right
        return root

    def tree_successor(self, node):
        if node.right:
            print('Exist')
            return self.tree_maximum(node.right)
        parent = node.p
        while parent and parent.left is node:
            node = parent
            parent = node.p
        if not node:
            print('Not exist')
            return
        print('Exist')
        return node

    def tree_presuccessor(self, node):
        if node.left:
            print('Exist')
            return self.tree_minimum(node.left)
        parent = node.p
        while parent and parent.right is not node:
            node = parent
            parent = node.p
        node = parent
        if not node:
            print('Not exist')
            return
        print('Exist')
        return node

    def tree_insert(self, node):
        self.tree[0] += 1
        y = None
        try:
            x = self.tree[1]
        except:
            x = None
        while x:  # 总是在叶子节点插入
            y = x
            if node.key > x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if not y:
            self.tree.insert(1, node)  # tree is empty
        elif node.key > y.key:
            y.left = node
        else:
            y.right = node
        if y:
            self.tree.append(node)

    def transpalnt(self, u, v):  # 用 v 子树来代替 u 子树
        if not u.p:
            self.tree.insert(1, v)
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p

    def tree_delete(self, node):
        self.tree[0] -= 1
        # 要删除结点没有两个孩子则直接替代
        if not node.left:
            self.transpalnt(node, node.right)
        elif not node.right:
            self.transpalnt(node, node.left)
        # 若有两个孩子
        else:
            y = self.tree_maximum(node.right)  # 找到要删除结点的后继，后继一定没有左孩子
            if y.p is not node:  # 如果 y 不是 node 的父结点，就要单独处理 y 的右子树
                # 用 y 右孩子代替 y
                self.transpalnt(y, y.right)
                # 处理 node 的右孩子
                y.right = node.right
                y.right.p = node
            # y 是 node 的父结点就不用单独处理
            self.transpalnt(node, y)
            # 处理 node 的左孩子
            y.left = node.left
            y.left.p = y


if __name__ == '__main__':
    T = []
    # for i in [6, 9, 5, 10, 7, None, 2, None, None, 8, None, None, None,
    #           3, 1, None, None, None, None, None, None, None, None,
    #           None, None, None, None, 4]:
    #     if i:
    #         T.append(Node(i))
    #     else:
    #         T.append(None)
    for i in [6, 9, 5, 10, 7, 2, 8, 3, 1, 4]:
        T.append(Node(i))
    bst = BinarySearchTree(T)
    bst.inorder_tree_walk(bst.tree[1])
    rst = bst.tree_search(bst.tree[1], 5)
    rst = bst.tree_search(bst.tree[1], 15)
    rst = bst.interactive_tree_search(bst.tree[1], 10)
    rst = bst.interactive_tree_search(bst.tree[2], 6)
    print('Maximum: ', bst.tree_maximum(bst.tree[3]).key)
    print('Minimum: ', bst.tree_minimum(bst.tree[2]).key)
    print('Successor: ', bst.tree_successor(bst.tree[10]).key)
    print('Successor: ', bst.tree_successor(bst.tree[1]).key)
    bst.tree_presuccessor(bst.tree[4])
    print('Presuccessor: ', bst.tree_presuccessor(bst.tree[1]).key)
    bst.tree_insert(Node(5.5))
    bst.tree_delete(bst.tree[1])
    print('Program ended!')
