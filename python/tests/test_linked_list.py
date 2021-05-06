from linked_list.linked_list import LinkedList, Node

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
   assert linked_list.head.value == 'a'
   linked_list.insert('c')
   assert linked_list.head.value == 'a'
   linked_list.insert('d')
   assert linked_list.head.value == 'a'
   assert linked_list.head.next.value == 'b'


# creating a Linked list to test the include method
linked_list = LinkedList()
new_nodes = ['I', 'am', 'here', 'and', ['a', 'l', 'i', 7, 3]]
for node in new_nodes:
    linked_list.insert(node)

def test_includes_true():
    assert linked_list.include('here') == True
    assert linked_list.include(['a', 'l', 'i', 7, 3]) == True
    assert linked_list.include('am') == True

def test_includes_false():
    assert linked_list.include('fff') == False
    assert linked_list.include([]) == False
    assert linked_list.include(4) == False

def test__str__method():
    assert linked_list.__str__() == "{ I } -> { am } -> { here } -> { and } -> { ['a', 'l', 'i', 7, 3] } ->  Null"