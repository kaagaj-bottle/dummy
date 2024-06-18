import sys
import os
import pytest


from fractions import Fraction

from pkgs import sum, multiply


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ([1, 2, 3, 4], 10),
        ([Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)], 1),
        ([1.1, 3.2], 4.3),
    ],
)
def test_sum(value, expected_result):
    assert sum(value) == expected_result


@pytest.mark.parametrize("value, expected_result", [([1, 2, 3], 6), ([0, 1, 24], 0)])
def test_multiply(value, expected_result):
    assert multiply(value) == expected_result