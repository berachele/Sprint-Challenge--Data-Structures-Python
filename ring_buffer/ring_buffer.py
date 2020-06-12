class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0

    def append(self, item):
        if self.size is self.capacity:
            print("TRIGGERING IF")
            # self.storage.pop(0)
            # self.storage.insert(0, item)
            self.storage.reverse()
            print(self.storage)
            self.storage.pop()
            print(self.storage)
            self.storage.append(item)
            print(self.storage)
            self.storage.reverse()
            print(self.storage)
        else:
            print("HITTING ELSE")
            self.storage.append(item)
            self.size += 1

    def get(self):
        return self.storage
