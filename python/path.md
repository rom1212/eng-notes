# Python Path
## realpath & abspath
```python
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Use abspath here to make sure that it works when the working directory is not the same as this file.
somedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
```
