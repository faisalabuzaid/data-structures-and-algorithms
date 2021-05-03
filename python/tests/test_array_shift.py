from code_challenges.array_shift.array_shift import insertShiftArray

def test_oddshift():
    input= [1,2,3,5,6]
    expected=[1, 2, 3, 4, 5, 6]
    actual = insertShiftArray(input, 4)
    assert actual == expected

def test_evenshift():
    input= [1,2,3,5,6,7]
    expected=[1, 2, 3, 4, 5, 6, 7]
    actual = insertShiftArray(input, 4)
    assert actual == expected
