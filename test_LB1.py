import unittest
from LB1 import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(3), pi * 3 ** 2)
        self.assertEqual(circle_area(1), 0)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi * 2.5 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -14)

    def test_type_date(self):
        self.assertRaises(TypeError, circle_area, [24])
        self.assertRaises(TypeError, circle_area, "string")
        self.assertRaises(TypeError, circle_area, True)
