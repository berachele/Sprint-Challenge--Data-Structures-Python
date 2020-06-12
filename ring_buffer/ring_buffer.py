class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, item):
        if self.size is self.capacity:
            print("TRIGGERING IF")
            oldest = self.head
            self.storage.pop(0)
            self.storage.insert(0, item)
            oldest += 1
        else:
            print("HITTING ELSE")
            self.storage.append(item)
            self.size += 1

    def get(self):
        return self.storage
