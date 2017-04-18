"""
树的做孩子右兄弟表示法
p 表示父节点
lchild 表示最左边的孩子
rsibling 表示兄弟节点（非最左边的孩子）
"""


class Node:

    def __init__(self):
        self.p = None
        self.lchild = None
        self.rsibling = None
        self.elem = None


class Tree:

    def __init__(self):
        self.root = None