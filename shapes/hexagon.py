import math
from .base import Shape

class Hexagon(Shape):
    def __init__(self, side):
        try:
            self.side = float(side)
        except ValueError:
            raise ValueError("边长必须为数字")
        if self.side <= 0:
            raise ValueError("边长必须为正数")

    def area(self) -> float:
        return (3 * math.sqrt(3) / 2) * (self.side ** 2)

    def perimeter(self) -> float:
        return 6 * self.side

    def parameters(self) -> dict:
        return {"side": self.side}
