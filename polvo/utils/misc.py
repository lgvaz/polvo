# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01t_utils.misc.ipynb.

# %% auto 0
__all__ = ['kwargs_grid']

# %% ../../nbs/01t_utils.misc.ipynb 2
import itertools

# %% ../../nbs/01t_utils.misc.ipynb 3
def kwargs_grid(**kwargs):
    "Returns a generator with all combinations of kwargs"
    return (dict(zip(kwargs.keys(), v)) for v in itertools.product(*kwargs.values()))