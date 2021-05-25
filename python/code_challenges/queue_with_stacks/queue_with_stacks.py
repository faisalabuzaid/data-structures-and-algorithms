class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack():
    def __init__(self, top=None):
        self.top = top
        self.next = None

    def push(self, new_value):
        node = Node(new_value)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    def pop(self):
        if self.top:
            prev = self.top
            self.top = self.top.next
            return prev.value
        else:
            raise Exception("You are trying to pop empty stack")
    
    def peek(self):
        if self.top:
            return self.top.value
        raise Exception("You can't peek an embty stack")

    def isEmpty(self):
        if not self.top:
            return True
        return False


class PsuedoQueue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, value):

    current = self.stack1.top
    while current:
      self.stack2.push(self.stack1.pop())
      current = current.next

    self.stack1.push(value)

    current_two = self.stack2.top
    while current_two:
      self.stack1.push(self.stack2.pop())
      current_two = current_two.next



  def dequeue(self):
    return str(f"[{self.stack1.pop()}]")

  def __str__(self):
    current = self.stack1.top
    items = []
    while current:
        items.append(str(f"<-[{current.value}]"))
        current = current.next
    return "".join(items)