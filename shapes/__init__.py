import unittest
import math

from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.parallelogram import Parallelogram
from shapes.rhombus import Rhombus
from shapes.trapezoid import Trapezoid
from shapes.hexagon import Hexagon
from shapes.circle import Circle


class TestShapes(unittest.TestCase):

    def test_triangle(self):
        t = Triangle(a=3, b=4, c=5)
        self.assertAlmostEqual(t.perimeter(), 12)
        self.assertAlmostEqual(t.area(), 6)

    def test_rectangle(self):
        r = Rectangle(length=4, width=5)
        self.assertEqual(r.perimeter(), 18)
        self.assertEqual(r.area(), 20)

    def test_square(self):
        s = Square(side=4)
        self.assertEqual(s.perimeter(), 16)
        self.assertEqual(s.area(), 16)

    def test_parallelogram(self):
        p = Parallelogram(base=6, height=4, side=5)
        self.assertEqual(p.area(), 24)
        self.assertEqual(p.perimeter(), 22)

    def test_rhombus(self):
        r = Rhombus(d1=6, d2=8, side=5)
        self.assertEqual(r.area(), 24)  # 1/2 * 6 * 8
        self.assertEqual(r.perimeter(), 20)

    def test_trapezoid(self):
        t = Trapezoid(base1=6, base2=10, height=4, side1=5, side2=5)
        self.assertEqual(t.area(), 32)  # (6+10)/2*4
        self.assertEqual(t.perimeter(), 26)

    def test_hexagon(self):
        h = Hexagon(side=6)
        expected_area = (3 * math.sqrt(3) / 2) * (6 ** 2)
        self.assertAlmostEqual(h.area(), expected_area)
        self.assertEqual(h.perimeter(), 36)

    def test_circle(self):
        c = Circle(radius=7)
        self.assertAlmostEqual(c.area(), math.pi * 49)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 7)


if __name__ == "__main__":
    unittest.main()
