import unittest

from src.point import Point

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        p = Point(10, 20)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 20)

if __name__ == "__main__":
    unittest.main()