class Stack:

    def __init__(self, size):

        self.S = [None for i in range(size)]
        self.top = 0
        self.size = size

    def stack_empty(self):
        if self.S[self.top]:
            return False
        return True

    def push(self, elem):
        if self.top + 1 >= self.size:
            print('overflow!')
            return None
        if not self.stack_empty():
            self.top += 1
        self.S[self.top] = elem

    def pop(self):
        if self.stack_empty():
            print('underflow!')
            return None
        elem = self.S[self.top]
        self.S[self.top] = None
        self.top -= 1
        return elem

if __name__ == '__main__':
    S = Stack(3)
    a = S.pop()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    b = S.pop()
    for i in S.S:
        print(i)

