# ndarray

## reshape
```
>>> import numpy as np
>>> a = np.arange(6)
>>> a
array([0, 1, 2, 3, 4, 5])
>>> np.reshape(a, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 232, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "/home/ubuntu/.local/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 57, in _wrapfunc
    return getattr(obj, method)(*args, **kwds)
ValueError: cannot reshape array of size 6 into shape (2,)
>>> np.reshape(a, (2, 3))
array([[0, 1, 2],
       [3, 4, 5]])
>>> a.reshape(2,3)
array([[0, 1, 2],
       [3, 4, 5]])
>>> a.reshape((2,3))
array([[0, 1, 2],
       [3, 4, 5]])
```

## frombuffer
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
