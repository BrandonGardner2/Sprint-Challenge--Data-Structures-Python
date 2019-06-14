class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.iterate()

    def get(self):
        return [i for i in self.storage if i != None]

    def iterate(self):
        if self.current == len(self.storage) - 1:
            self.current = 0
        else:
            self.current += 1
