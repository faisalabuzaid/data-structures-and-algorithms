from code_challenges.ll_zip.ll_zip import *
import pytest

def test_1slist_shorter():
    l_list1 = create_list(['d', 'c', 'b', 'a'])
    l_list2 = create_list(['h','g','f','e','z'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == 'a, z, b, e, c, f, d, g, h'

def test_1slist_longer():
    l_list1 = create_list(['d', 'c', 'b', 'a', 'z'])
    l_list2 = create_list(['h','g','f','e'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == "z"
    assert l_list1.__str__() == 'z, e, a, f, b, g, c, h, d'

def test_lists_equal():
    l_list1 = create_list(['d', 'c', 'b', 'a'])
    l_list2 = create_list(['h','g','f','e'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == 'a, e, b, f, c, g, d, h'

def test_lists_empty():
    l_list1 = LinkedList()
    l_list2 = LinkedList()
    with pytest.raises(Exception):
        zip_list(l_list1, l_list2)

def test_list_1st_empty():
    l_list1 = LinkedList()
    l_list2 = create_list(['d', 'c', 'b', 'a'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == 'a, b, c, d'

def test_list_2nd_empty():
    l_list2 = LinkedList()
    l_list1 = create_list(['d', 'c', 'b', 'a'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == 'a, b, c, d'

def test_list_1st_1element():
    l_list1 = create_list([1])
    l_list2 = create_list(['d', 'c', 'b', 'a'])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 1
    assert l_list1.__str__() == '1, a, b, c, d'

def test_list_2ndlist_1element():
    l_list1 = create_list(['d', 'c', 'b', 'a'])
    l_list2 = create_list([1])
    ref_to_head = zip_list(l_list1, l_list2)
    assert ref_to_head.value == 'a'
    assert l_list1.__str__() == 'a, 1, b, c, d'