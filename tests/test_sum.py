import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fractions import Fraction

from pkgs.s1 import mod1


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ([1, 2, 3, 4], 10),
        ([Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)], 1),
        ([1.1, 3.2], 4.3),
    ],
)
def test_sum(value, expected_result):
    assert mod1.sum(value) == expected_result
