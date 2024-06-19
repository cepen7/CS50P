from bank import value

def test_hello():
    assert value("hello") == 0

def test_initial_h():
    assert value("How you doing?") == 20

def test_noH():
    assert value("G'day, mate") == 100
