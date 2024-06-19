from plates import is_valid

def test_first_two_letters():
    assert is_valid("AB") == True


def test_length():
    assert is_valid("OK12345") == False


def test_just_nums_and_abc():
    assert is_valid("SEX?") == False


def test_first_num():
    assert is_valid("OKU0") == False
