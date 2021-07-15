# Timovar
Python variables with timeout

# What it does?
You can easily create variables with specific timeout. After this time
you can check it and if neccessary remove.

## examples of usage

* TimeoutVar
This is the basic class. You can easily create the timeout variable:

```python
from timovar import TimeoutVar as TV
var = TV(3)
```

* TimeoutDict
This is the extension of the basic class

```python
from timovar import TimeoutDict as TD
your_dict = TD({"1": 1, "3": 3})
print(your_dict) # {1: 1, 3: 3}
```

you can easily add new values to your timeout dict
```python
your_dict.append({"2": 2})
print(your_dict) # {1: 1, 2: 2, 3: 3}
```

But don't forget that these values can be extracted only in the timeout period.
For example:
```python
import time
from timovar import TimeoutDict as TD


_dict = TD({"3": 3, "4": 4})

print(_dict["3"])
time.sleep(3)
print(_dict)
_dict.append({"6": 6})
print(_dict)
print(_dict["3"])
time.sleep(3)
print(_dict)
time.sleep(5)
print(_dict)
```

