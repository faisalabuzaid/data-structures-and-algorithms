class EmptyStackException(Exception):
  pass
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
            raise EmptyStackException("You are trying to pop empty stack")
    
    def peek(self):
        if self.top:
            return self.top.value
        raise EmptyStackException("You can't peek an embty stack")

    def isEmpty(self):
        if not self.top:
            return True
        return False

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)



class Queue():
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node  = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front:
            prev = self.front
            self.front = self.front.next
            return prev.value
        raise EmptyQueueException("You can't dequeue from empty Queue")

    def peek(self):
        if self.front:
            return self.front.value
        raise EmptyQueueException("Empty Queue")


    def isEmpty(self):
        if not self.front:
            return True
        return False

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)




if __name__ == "__main__":
    pass
