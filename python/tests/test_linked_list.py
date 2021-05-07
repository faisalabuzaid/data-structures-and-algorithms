import pytest
from code_challenges.data_structures.linked_list.linked_list import LinkedList, Node

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_Node_created():
    assert "f" == Node('f').value
    assert None == Node('f').next

def test_insert_to_empty():
    val = 'test'
    linked_list = LinkedList()
    linked_list.insert(val)
    assert linked_list.head.value == 'test'

def test_head_to_the_first_el():
   linked_list = LinkedList()
   linked_list.insert('a')
   assert linked_list.head.value == 'a'
   linked_list.insert('b')
   assert linked_list.head.value == 'b'
   linked_list.insert('c')
   assert linked_list.head.value == 'c'
   linked_list.insert('d')
   assert linked_list.head.value == 'd'
   assert linked_list.head.next.value == 'c'


# creating a Linked list to test the include method
@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    new_nodes = ['I', 'am', 'here', 'and', ['a', 'l', 'i', 7, 3]]
    for node in new_nodes:
        linked_list.insert(node)
    return linked_list

def test_includes_true(linked_list):
    assert linked_list.include('here') == True
    assert linked_list.include(['a', 'l', 'i', 7, 3]) == True
    assert linked_list.include('am') == True

def test_includes_false(linked_list):
    assert linked_list.include('fff') == False
    assert linked_list.include([]) == False
    assert linked_list.include(4) == False

def test__str__method(linked_list):
    assert linked_list.__str__() == "{ ['a', 'l', 'i', 7, 3] } -> { and } -> { here } -> { am } -> { I } ->  Null"