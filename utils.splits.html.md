# Splits


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/splits.py#L13"
target="_blank" style="float:right; font-size:smaller">source</a>

### random

>      random (items, probs, seed=None)

``` python
random(list(range(10)), [0.8, 0.1, 0.1])
```

    [[6, 9, 3, 5, 7, 1, 4, 2], [8], [0]]

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/splits.py#L28"
target="_blank" style="float:right; font-size:smaller">source</a>

### from_fn

>      from_fn (items, fn)

*`fn` should return the index for each subset*

``` python
from_fn(list(range(10)), lambda x: 0 if x>4 else 1)
```

    ([5, 6, 7, 8, 9], [0, 1, 2, 3, 4])