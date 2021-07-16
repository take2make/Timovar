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
For example (each value has the lifetime = 5 seconds):
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
## Update (version with redis as a backgroud worker)

In the previous version you should to remove variables by yourself, in this
update this work can be done by redis. 
Firstly, you should install redis package
```bash
pip3 install redis
```

Now you can apply new abstraction:
```python
from timovar import TimeoutRedisVar as TRV
from timovar import SomeVar # it can be any specific object
import redis

redis = redis.Redis(
        host= 'localhost',
        port= '6379')
        
Agents = TRV(redis)
Agents["1"] = SomeVar(1) # define

print(Agents["1"].value)
time.sleep(0.6)

Agents["1"] = SomeVar(2) # redefine
print(Agents["1"].value)
time.sleep(0.6)

print(Agents["1"].value)
time.sleep(1.9)

print(Agents["1"].value) # will be none, because default timeout is 1 second



