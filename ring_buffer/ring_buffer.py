class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.oldest = len(self.storage)-len(self.storage)

    def append(self, item):
        if self.size == self.capacity:
            print("TRIGGERING IF")
            print(self.oldest)
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            self.oldest += 1
            print(self.oldest)
        else:
            print("HITTING ELSE")
            self.storage.append(item)
            self.size += 1

    def get(self):
        return self.storage
