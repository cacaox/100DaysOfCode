import unittest

class TestFunc(unittest.TestCase):
    def test_func(self):
        from test import func
        self.assertIsNone(func('ドコドコ'))