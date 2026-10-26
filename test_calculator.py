def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_neg_and_pos():
    assert add(3, -4) == -1

def test_subtract():
    assert 4 - 3 == 1
