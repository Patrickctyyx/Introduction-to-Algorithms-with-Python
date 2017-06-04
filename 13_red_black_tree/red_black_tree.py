"""
root.left.key < root < root.right.key
"""

RED = 'RED'
BLACK = 'BLACK'


class Node:

    def __init__(self, key):
        self.key = key
        self.color = BLACK
        self.left = None
        self.right = None
        self.p = None


class RedBlackTree:

    def __init__(self):
        self.root = None
        self.nil = Node(None)

    def left_rotate(self, x):
        if x.right == self.nil:
            print('This node cannot be rotated!')
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.left = x
        if x.p == self.nil:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.p = x.p
        x.p = y

    def right_rotate(self, x):
        if x.left == self.nil:
            print('This node cannot be rotated!')
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.right = x
        if x.p == self.nil:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.p = x.p
        x.p = y

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key > x.key:
                x = x.right
            else:
                x = x.left
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        # 违反了性质 4 才循环
        # 不可能有多个节点时插入到根结点，因此性质 2 不会违反
        while z.p.color == RED:
            # 根据 z.p 是 z.p.p 的左右结点分为两种情况
            if z.p == z.p.p.left:
                # y 为 z.p 的兄弟结点
                y = z.p.p.right
                # 情况一，z 的叔叔结点也是红色
                if y.color == RED:
                    # 直接把父节点设置为黑色
                    z.p.color = BLACK
                    # 为了保护性质 5 把另外两个也改了
                    y.color = BLACK
                    z.p.p.color = RED
                    # z 向上挪到红色结点
                    # 这里结束之后可能违反性质 5 也可能违反性质 2，但不会同时违反
                    z = z.p.p
                # 情况二，z 的叔叔结点是黑色并且 z 是右孩子
                elif z == z.p.right:
                    # 直接左转变成情况三，当然 z 要向上移动一位
                    z = z.p
                    self.left_rotate(z)
                # 情况三，z 的叔叔结点是黑色并且 z 是左孩子
                # 直接把父节点设置为黑
                z.p.color = BLACK
                # 为了保护性质 4 祖父结点设置为红
                z.p.p.color = RED
                # 为了保护 z 叔叔结点一侧的性质 5，向右旋转
                # 这样 z.p 一定是黑了
                self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(z)
                z.p.color = BLACK
                z.p.p.color = RED
                self.left_rotate(z.p.p)
        # 如果直接在跟结点插入
        # 那么原来树为空
        # 此时违反了性质 2，于是这里改过老
        self.root.color = BLACK
