class Queue:
    inner_list = []
    counter = 0

    def __init__(self):
        self.length = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.counter, value)
        self.counter = self.counter + 1
        self.length = self.length + 1
        
    def dequeue(self):
        self.counter = self.counter - 1
        value = self.inner_list.pop(0)
        self.length = self.length - 1
        return(value)
    
    def size(self):
        return self.length

    def delete(self, value):
        l = []
        while self.size() > 0:
            l.append(self.dequeue())
        l.remove(value)
        i = 0
        while i < len(l):
            if l[i] == value:
                l.pop(i)
            i = i + 1
        for j in range(len(l)):
            self.enqueue(l[j])
            


obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue())
