def flatten(iterable):
    """Flattens an iterable."""
    for i in iterable:
        try:
            yield from flatten(i)
        except TypeError:
            yield i