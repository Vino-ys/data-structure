class Stack:
    def __init__(self , size: int):
        self.size = size
        self.top = -1
        self.arr = [None for _ in range(size)]

    def isFull(self): return self.top == self.size - 1

    def isEmpty(self): return self.top == -1

    def push(self, data):
        if self.isFull():
            print('스택이 가득참;')
            return
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        if self.isEmpty():
            print('스택이 비어있음;;')
            return
        
        a = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return a
    
    #완벽 ㅋㅋㅋㅋ