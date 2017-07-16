# ndarray
```
>>> import numpy as np
>>> s = 'hello world'
>>> a = np.frombuffer(s, dtype='S1')
>>> type(a)
<type 'numpy.ndarray'>
>>> b = np.frombuffer(s, dtype=np.uint8)
>>> b
array([104, 101, 108, 108, 111,  32, 119, 111, 114, 108, 100], dtype=uint8)
>>> type(b)
<type 'numpy.ndarray'>
```
