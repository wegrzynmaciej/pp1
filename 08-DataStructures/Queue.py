class Queue():

    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        v = self.queue[0]
        del self.queue[0]
        return v
