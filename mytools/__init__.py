from itertools import islice


def flatten(iterable):
    """Flattens an iterable."""
    for i in iterable:
        try:
            yield from flatten(i)
        except TypeError:
            yield i


def chunk(flat_list, sizes):
    """Breaks a list into chunks - sort of the opposite of flatten."""
    iter_flat = iter(flat_list)
    yield from (list(islice(iter_flat, 0, size)) for size in sizes)
