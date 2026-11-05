import unittest

from greeting import greet


class TestGreet(unittest.TestCase):
    def test_returns_greeting(self):
        self.assertEqual(greet("Qursam"), "Hello, Qursam!")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
