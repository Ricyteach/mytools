# mytools
A haphazard collection of python tools/utilities that aren't specific to any project.

Install:

```bash
pip install git+https://github.com/Ricyteach/mytools
```

Flatten an iterable:

```python
>>> from mytools import flatten
>>> list(flatten([1,[1,2,[1,2],[1,2]],2,3,[[1,2],1,[1,2]],4]))
[1, 1, 2, 1, 2, 1, 2, 2, 3, 1, 2, 1, 1, 2, 4]
```