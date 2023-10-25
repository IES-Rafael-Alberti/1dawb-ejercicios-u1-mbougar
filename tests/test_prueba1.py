from tests.prueba1 import encontrarMayor
import pytest

def test_encontrarMayor():
    assert encontrarMayor(1, 1) == 0
    assert encontrarMayor(2, 0) == 2
    assert encontrarMayor(-100, 100) == 100

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8),
        (9, encontrarMayor(3, 18), 18)
    ]
)
def test_encontrarMayor_params(input_n1, input_n2, expected):
    assert encontrarMayor(input_n1, input_n2) == expected