
# import inittest package na functions we want to test out
import unittest
from sqrt import lazy_sqrt, built_sqrt, newton_sqrt1

class SqrtTests(unittest.TestCase):
    """Obligatory docstring test squere root finctions"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(lazy_sqrt(2)**2, 2)

class SquaringTests(unittests.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()