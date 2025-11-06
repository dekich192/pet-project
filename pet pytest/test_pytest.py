from nemain import Calculator
import pytest


@pytest.mark.parametrize(
    "a, b, res",
    [
        (1, 2, 0.5),
        (2, 2, 1),                    #мой первый тест который прокнул
        (3, 2, 1.5),
    ]
    )
def test_divide(a, b, res):
    assert Calculator().divide(a, b) == res