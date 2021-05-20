from code_challenges.stacks_and_queues.stacks_and_queues import Node, Stack, Queue
import pytest

@pytest.fixture
def test_stack():
    test_stack = Stack()
    """helper function to create a stack"""
    test = [1, 2, 3, 4]
    for el in test:
        test_stack.push(el)
    return test_stack

def test_stack_empty():
    empty_stack = Stack()
    assert empty_stack.top == None

def test_stack_push(test_stack):

    test_stack.push(5)
    assert test_stack.top.value == 5
    test_stack.push('b')
    assert test_stack.top.value == 'b'
    test_stack.push('c')
    assert test_stack.top.value == 'c'

def test_stack_pop(test_stack):
    assert test_stack.pop() == 4
    assert test_stack.top.value == 3
    assert test_stack.top.next.value == 2
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.top == None

def test_stack_peek(test_stack):
    assert test_stack.peek() == 4
    test_stack.pop()
    assert test_stack.peek() == 3
    test_stack.pop()
    test_stack.pop()
    assert test_stack.peek() == 1

def test_stack_is_empty(test_stack):
    embty_stack = Stack()
    assert embty_stack.isEmpty() == True
    assert test_stack.isEmpty() == False

@pytest.fixture
def test_queue():
    test_queue = Queue()
    nodes = ['a', 'b', 'c', 'd']
    for el in nodes:
        test_queue.enqueue(el)
    return test_queue


def test_queue_empty():
    test_queue = Queue()
    assert test_queue.front == None
    assert test_queue.rear == None

def test_queue_enqueu():
    test_queue = Queue()
    assert test_queue.front == None
    test_queue.enqueue(5)
    assert test_queue.front.value == 5
    test_queue.enqueue('b')
    assert test_queue.rear.value == 'b'
    assert test_queue.front.value == 5
    test_queue.enqueue('c')
    assert test_queue.rear.value == 'c'
    assert test_queue.front.value == 5

def test_queue_dequeue(test_queue):
    assert test_queue.dequeue() == 'a'
    assert test_queue.front.value == 'b'
    assert test_queue.front.next.value == 'c'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.front == None

def test_queue_peek(test_queue):
    assert test_queue.peek() == 'a'
    test_queue.dequeue()
    assert test_queue.peek() == 'b'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.front == None

def test_queue_is_empty(test_queue):
    assert test_queue.isEmpty() == False
    test_queue = Stack()
    assert test_queue.isEmpty() == True

def test_queue_one_el(test_queue):
    assert test_queue.isEmpty() == False
    assert test_queue.rear.value == "d"
    assert test_queue.front.value == "a"