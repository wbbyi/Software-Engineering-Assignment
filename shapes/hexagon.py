import math
from .base import Shape

class Hexagon(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return (3 * math.sqrt(3) / 2) * (self.side ** 2)

    def perimeter(self) -> float:
        return 6 * self.side

    def __str__(self):
        return f"Hexagon(side={self.side})"

    def parameters(self):
        return {"side": self.side}
