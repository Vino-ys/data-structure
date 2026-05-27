class Stack:
  def __init__(self, size: int):
    self.size = size
    self.top = -1
    self.arr = [None for _ in range(size)]

  def isempty(self): return self.top == -1
  def isfull(self): return self.top == self.size - 1

  def push(self, data):
    if self.isfull():
      print('스택이 가득찼잖냐')
      return
    self.top += 1
    self.arr[self.top] = data

  def pop(self):
    if self.isempty():
      print('스택이 비었슴다')
      return
    a = self.arr[self.top]
    self.arr[self.top] = None
    self.top -= 1
    return a


stack = Stack(5)
print(stack.arr)
stack.push(1)
print(stack.arr)
stack.push(1)
print(stack.arr)
stack.push(1)
print(stack.arr)
stack.push(1)
print(stack.arr)
stack.push(1)
print(stack.arr)
stack.push(1)

stack.pop()
print(stack.arr)
stack.pop()
print(stack.arr)
stack.pop()
print(stack.arr)
stack.pop()
print(stack.arr)
stack.pop()
print(stack.arr)
stack.pop()