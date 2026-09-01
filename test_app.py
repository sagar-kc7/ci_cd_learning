from app import add


def test_add():
    assert add(2, 3) == 2
    assert add(-1, 1) == 0
    assert add(0, 1) == 1
    assert add(-5, -5) == -10