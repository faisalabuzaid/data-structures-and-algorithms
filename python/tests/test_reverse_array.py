from code_challenges.array_reverse.array_reverse import reverseArray

def test_array():

    except1 = [5, 4, 3, 2, 1]
    except2 = [-1, 844, 12, 0, 2, 51, 1590, 77]
    actual1 = reverseArray([1, 2, 3, 4, 5])
    actual2 = reverseArray([77, 1590, 51, 2, 0, 12, 844, -1])
    assert  actual1 == except1
    assert  actual2 == except2