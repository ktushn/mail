import pytest


def test_set_1():
    assert 1 in {1, 2, 3}


def test_set_2():
    a = {1, 2, 3}
    a.add(4)
    assert a == {1, 2, 3, 4}


def test_set_3():
    try:
        assert {1, 2} + {3, 4} == {1, 2, 3, 4}
    except TypeError:
        pass


def test_tuple_1():
    a = (1, 2, 3)
    assert a[1] == 2


@pytest.mark.parametrize("test_input,expected", [((1, 2, 3), 3), ((4, 5), 2), ((), 0)])
def test_tuple_2(test_input, expected):
    assert len(test_input) == expected


def test_tuple_3():
    assert (1, 2, 1, 2, 1, 2).count(1) == 3
