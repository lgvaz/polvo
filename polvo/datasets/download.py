# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/02f_datasets.download.ipynb.

# %% auto 0
__all__ = ['snacks_tiny']

# %% ../../nbs/02f_datasets.download.ipynb 2
import polvo as pv

# %% ../../nbs/02f_datasets.download.ipynb 3
# TODO: This just goes to tmp folder
def snacks_tiny():
    data_dir = pv.mkdir('snacks', tmp=True, exist_ok=True, overwrite=True)
    data_dir = pv.download_and_extract('https://github.com/lgvaz/polvo-datasets-hub/releases/download/snacks/snacks.zip',
                                       data_dir)
    return data_dir
