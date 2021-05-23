from code_challenges.queue_with_stacks.queue_with_stacks import Node, Stack, PsuedoQueue
import pytest

@pytest.fixture
def queue_list():
    test_list = [5, 10, 15, 20]
    test_queue = PsuedoQueue()
    for i in test_list:
        test_queue.enqueue(i)
    
    return test_queue


def test_enqueue_to_empty():
    test = PsuedoQueue()
    test.enqueue(5)
    actual = test.__str__()
    expected = "<-[5]"
    assert actual == expected

def test_enqueue(queue_list):
    queue_list.enqueue(25)
    actual = queue_list.__str__()
    excepted = "<-[5]<-[10]<-[15]<-[20]<-[25]"
    assert actual == excepted

def test_dequeue(queue_list):
    pop_1_value = queue_list.dequeue()
    pop_2_value = queue_list.dequeue()
    pop_3_value = queue_list.dequeue()
    pop_4_value = queue_list.dequeue()
    actual = [pop_1_value, pop_2_value, pop_3_value, pop_4_value]
    excepted = ["[5]", "[10]", "[15]", "[20]"]
    assert actual == excepted