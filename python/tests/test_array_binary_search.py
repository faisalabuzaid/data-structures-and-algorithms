from code_challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary():
    actual1 = BinarySearch([50,90,120,500], 0)
    actual2 = BinarySearch([50,90,120,500], 3)
    actual3 = BinarySearch([50,90,120,500], 5)
    expected1 = 50
    expected2 = 500
    expected3 = -1
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3

