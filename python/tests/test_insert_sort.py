from code_challenges.insert_sort.insert_sort import sort

def test_sort_one():
    test = [5, 4, 3, 2]
    sort(test)
    actual = test
    expected = [2, 3, 4, 5]
    assert actual == expected

def test_sort_two():
    test = [10, 20, 3, 40]
    sort(test)
    actual = test
    expected = [3, 10, 20, 40]
    assert actual == expected
