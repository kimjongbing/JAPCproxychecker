import threading

class Counter:
    def __init__(self):
        self.val = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.val += 1

    def value(self):
        with self._lock:
            return self.val