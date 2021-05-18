import pytest
from data_structures.linked_list.linked_list import LinkedList, Node

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

def test_kthFromEnd(linked_list):
    actual = linked_list.kthFromEnd(1)
    excpected = 'am'
    assert excpected == actual

def test_kthFromEnd2(linked_list):
    # print(linked_list)
    actual = linked_list.kthFromEnd(88)
    print(actual)
    excpected = 'Sorry, the value is larger than the linked list'
    assert excpected == actual

def test_append(linked_list):
    assert "d, 4, b, a, z" == linked_list.append('z')

def test_append_to_empty(linked_list):
    assert "z" == linked_list.append('z')

def test_insert_before_value_in_list(linked_list):
    actual = linked_list.insert_before("and", 3)
    expected = "{ ['a', 'l', 'i', 7, 3] } -> { 3 } -> { and } -> { here } -> { am } -> { I } ->  Null"

    assert actual == expected

def test_insert_before_value_not_in_list(linked_list):
    assert 'Value is not in the list' == linked_list.insert_before('e', 3)

def test_insert_before_to_empty_list(linked_list):
    assert 'Value is not in the list' == linked_list.insert_before('e', 3)

def test_insert_after_value_in_list(linked_list):

    assert "d, 4, b, 3, cat, a, z" == linked_list.insert_after(3, 'cat')

def test_insert_after_value_not_in_list(linked_list):
    assert 'Value is not in the list' == linked_list.insert_after('e', 3)

def test_insert_after_to_empty_list(linked_list):
    assert 'Value is not in the list' == linked_list.insert_before('e', 3)

# def test_append_2(linked_list):
#     assert "d, 4, b, 3, cat, a, z, z2" == linked_list.append('z2')
#     assert "d, 4, b, 3, cat, a, z, z2, e2" == linked_list.append('e2')

def test_insert_before_node_in_the_middle(linked_list):
    assert "d, 4, b, 3, 123, cat, a, z, z2, e2" == linked_list.insert_before('cat', 123)

def test_insert_before_first_node(linked_list):
    assert "new_first, d, 4, b, 3, 123, cat, a, z, z2, e2" == linked_list.insert_before('d', "new_first")


def test_insert_after_the_middle(linked_list):
    assert "new_first, d, 4, b, 3, 123, cat, dog, a, z, z2, e2" == linked_list.insert_after('cat', 'dog')

def test_insert_after_the_last(linked_list):
    assert "new_first, d, 4, b, 3, 123, cat, dog, a, z, z2, e2, 1000" == linked_list.insert_after('e2', '1000')