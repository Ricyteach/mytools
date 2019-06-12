from typing import Iterable

from mytools import flatten, chunk


def test_flatten():
    assert not any(isinstance(x, Iterable) for x in flatten([1, 1, 2, [1, 2], [1, 2], 2, 3, [1, 2], 1, [1, 2], 4]))


def test_chunk():
    assert list(chunk([1,2,3,4,5], [2,3])) == [[1,2],[3,4,5]]
