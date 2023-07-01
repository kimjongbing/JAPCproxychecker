import unittest
from src.counter import Counter

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_increment(self):
        self.counter.increment()
        self.assertEqual(self.counter.value(), 1)

    def test_initial_value(self):
        self.assertEqual(self.counter.value(), 0)

if __name__ == '__main__':
    unittest.main()