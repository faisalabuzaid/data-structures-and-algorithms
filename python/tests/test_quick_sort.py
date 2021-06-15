from code_challenges.quick_sort.quick_sort import quick_sort

def test_sort_one():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    expected = [1, 5, 7, 8, 9, 10]
    assert arr == expected

def test_sort_two():
    arr = [1, 7, 8, 9, 11, 5]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    expected = [1, 5, 7, 8, 9, 11]
    assert arr == expected