# Get image size


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

``` python
import polvo as pv
from fastcore.all import *
```

    /home/lgvaz/git/polvo/polvo/utils/logging.py:8: TqdmExperimentalWarning: Using `tqdm.autonotebook.tqdm` in notebook mode. Use `tqdm.tqdm` instead to force console mode (e.g. in jupyter console)
      from tqdm.autonotebook import tqdm

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/image_size.py#L30"
target="_blank" style="float:right; font-size:smaller">source</a>

### UnknownImageFormat

*Common base class for all non-exit exceptions.*

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/image_size.py#L45"
target="_blank" style="float:right; font-size:smaller">source</a>

### Image

>      Image (path, type, file_size, width, height)

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/image_size.py#L108"
target="_blank" style="float:right; font-size:smaller">source</a>

### get_image_metadata_from_bytesio

>      get_image_metadata_from_bytesio (input, size, file_path=None)

\*Return an
[`Image`](https://lgvaz.github.io/polvo/utils.image_size.html#image)
object for a given img file content - no external dependencies except
the os and struct builtin modules

Args: input (io.IOBase): io object support read & seek size (int): size
of buffer in byte file_path (str): path to an image file

Returns: Image: (path, type, file_size, width, height)\*

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/image_size.py#L90"
target="_blank" style="float:right; font-size:smaller">source</a>

### get_image_metadata

>      get_image_metadata (file_path)

\*Return an
[`Image`](https://lgvaz.github.io/polvo/utils.image_size.html#image)
object for a given img file content - no external dependencies except
the os and struct builtin modules

Args: file_path (str): path to an image file

Returns: Image: (path, type, file_size, width, height)\*

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/image_size.py#L77"
target="_blank" style="float:right; font-size:smaller">source</a>

### image_size_from_bytesio

>      image_size_from_bytesio (input, size)

\*Return (width, height) for a given img file content - no external
dependencies except the os and struct builtin modules

Args: input (io.IOBase): io object support read & seek size (int): size
of buffer in byte\*

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/visualization.py#L98"
target="_blank" style="float:right; font-size:smaller">source</a>

### image_size

>      image_size (file_path)

*Return (width, height) for a given img file content - no external
dependencies except the os and struct builtin modules*

``` python
test_eq(image_size(pv.test.SEG_IMAGE), (500, 332))
```