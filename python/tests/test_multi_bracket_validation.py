from code_challenges.multi_bracket_validation.multi_bracket_validation import brackets_validation

def test_brackets_validation_curly():
    expected = True
    actual = brackets_validation("{}")
    assert actual == expected

def test_brackets_validation_parenthes():
    expected = True
    actual = brackets_validation("()")
    assert actual == expected

def test_brackets_validation_brackets():
    expected = True
    actual = brackets_validation("[]")
    assert actual == expected

def test_brackets_validation_Curly_with_parenthes():
    expected = True
    actual = brackets_validation("{}(){}")
    assert actual == expected

def test_brackets_validation_curly_with_double_brackets():
    expected = True
    actual = brackets_validation("(){}[[]]")
    assert actual == expected

def test_brackets_validation_brackets_with_string():
    expected = True 
    actual = brackets_validation("{}{Code}[Fellows](())")
    assert actual == expected

def test_brackets_validation_all():
    expected = True
    actual = brackets_validation("(){}[[]]")
    assert actual == expected

def test_brackets_validation_missing_one_bracket():
    expected = False 
    actual = brackets_validation("(](")
    assert actual == expected

def test_brackets_validation_parenthes_inside_curly():
    expected = False
    actual = brackets_validation("{(})")
    assert actual == expected

def test_brackets_validation_one_opening_curly():
    expected = False
    actual = brackets_validation("{")
    assert actual == expected

def test_brackets_validation_different_closing_opening():
    expected = False
    actual = brackets_validation("[)")
    assert actual == expected

def test_brackets_validation_one_closing_parenthes():
    expected = False
    actual = brackets_validation(")")
    assert actual == expected

def test_brackets_validation_string_with_closing_opening_different():
    expected = False
    actual = brackets_validation("{sadsad)")
    assert actual == expected

def test_brackets_validation_string_with_one_closing_parenthes():
    expected = False
    actual = brackets_validation("fsads(")
    assert actual == expected