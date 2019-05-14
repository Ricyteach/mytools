from typing import Iterable

from mytools import flatten

def test_flatten():
    assert not any(isinstance(x, Iterable) for x in flatten([1, 1, 2, [1, 2], [1, 2], 2, 3, [1, 2], 1, [1, 2], 4]))
