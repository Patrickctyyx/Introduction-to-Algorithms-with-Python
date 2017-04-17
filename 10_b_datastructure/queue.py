class Queue:

    def __init__(self, size):
        self.Q = [None for i in range(size + 1)]
        self.size = size + 1
        self.head = 0
        self.tail = 0

    def enqueue(self, elem):
        if (self.tail + 1) % self.size == self.head:
            print('overflow!')
            return None
        self.Q[self.tail] = elem
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.tail == self.head:
            print('underflow')
            return None
        elem = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % self.size
        return elem

if __name__ == '__main__':
    Q = Queue(3)
    a = Q.dequeue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    for i in Q.Q:
        print(i)
    b = Q.dequeue()
    print(b)