import unittest
from circle import circle_area
from math import pi
class TestCirclearea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
