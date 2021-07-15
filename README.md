# Timovar
Python variables with timeout

# What it does?
You can easily create variables with specific timeout. After this time
you can check it and if neccessary remove.

## examples of usage

* TimeoutVar
This is the basic class. You can easily create the timeout variable:

from timovar import TimeoutVar as TV
var = TV(3)

* TimeoutDict
This is the extension of the basic class

from timovar import TimeoutDict as TD
your_dict = TD({"1": 1, "3": 3})
print(your_dict) // {1: 1, 3: 3}

you can easily add new values to your timeout dict
your_dict.append({"2": 2})
print(your_dict) // {1: 1,2:2, 3: 3}
