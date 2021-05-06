from code_challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary():
    actual1 = BinarySearch([50,90,120,500], 50)
    actual2 = BinarySearch([50,90,120,500], 500)
    actual3 = BinarySearch([50,90,120,500], 600)
    expected1 = 0
    expected2 = 3
    expected3 = -1
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3

