from hashtable.hashtable import HashMap,Node,LinkedList

def test_hashtable_hash():
    hm = HashMap()
    actual = hm._hash("1")
    expected = 931
    assert actual == expected

def test_hashtable_add():
    hm = HashMap()
    hm.add("1", "sachin")
    actual = hm.get("1")
    expected = "sachin"
    assert actual == expected

def test_hashtable_get():
    hm = HashMap()
    hm.add("1", "sachin")
    actual = hm.get('1')
    expected = 'sachin'
    assert actual == expected

def test_hashtable_get_null():
    hm = HashMap()
    actual = hm.get("5")
    expected = 'Null'
    assert actual == expected

def test_hashtable_handle_collision():
    hashtable = HashMap()
    hashtable.add('ab', 'faisal')
    hashtable.add('ba', 'ahmad')
    acutal = hashtable.get('ab')
    acutal_two = hashtable.get('ba')
    expected = 'faisal'
    expected_two = 'ahmad'
    assert hashtable._hash('ab') == hashtable._hash('ba')
    assert acutal == expected
    assert acutal_two == expected_two

def test_hashtable_contains():
    hm = HashMap()
    hm.add("test", "this test contains")
    actual = hm.contains("test")
    expected = True
    actual_two = hm.contains("test_two")
    expected_two = False
    assert actual == expected
    assert actual_two == expected_two


