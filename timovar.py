import time


class TimeoutVar:
    """Variable whose values time out."""

    def __init__(self, value, timeout=5):
        """Store the timeout and value."""
        self._value = value
        self._last_set = time.time()
        self.timeout = timeout

    @property
    def value(self):
        """Get the value if the value hasn't timed out."""
        if time.time() - self._last_set < self.timeout:
            self._last_set = time.time()
            return self._value

    @value.setter
    def value(self, value, timeout=None):
        """Set the value while resetting the timer."""
        self._value = value
        self._last_set = time.time()
        if timeout is not None:
            self.timeout = timeout

    def __repr__(self):
        return f"{self._value}"

    def need_to_remove(self) -> bool:
        if time.time() - self._last_set < self.timeout:
            return False
        return True


class TimeoutDict:
    """Variable whose values time out."""

    def __init__(self, _dict, timeout=5):
        """
            Store the timeout and value.
            set timeout for each value of _dict
        """
        self.dict = {}
        for key, value in _dict.items():
            self.dict[key] = TimeoutVar(value)

    def __getitem__(self, key):
        for k, v in self.dict.copy().items():
            if self.dict[k].need_to_remove():
                del self.dict[k]

        return self.dict[key].value

    def __repr__(self) -> str:
        for k, v in self.dict.copy().items():
            if self.dict[k].need_to_remove():
                del self.dict[k]

        return f"{self.dict}"

    def append(self, mini_dict):
        item = list(mini_dict.items())[0]
        self.dict[item[0]] = TimeoutVar(item[1])