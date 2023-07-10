import threading


class Counter:
    def __init__(self):
        self.vals = {"Checked": 0, "Succeeded": 0, "Failed": 0}
        self._lock = threading.Lock()

    def increment(self, key):
        with self._lock:
            self.vals[key] += 1

    def value(self, key):
        with self._lock:
            return self.val[key]

    def values(self):
        with self._lock:
            return self.vals.copy()
