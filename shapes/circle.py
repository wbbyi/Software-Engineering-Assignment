import math
from .base import Shape

class Circle(Shape):
    def __init__(self, radius):
        try:
            radius = float(radius)
        except ValueError:
            raise ValueError("半径必须为数字")
        if radius <= 0:
            raise ValueError("半径必须大于 0")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def parameters(self) -> dict:
        return {"radius": self.radius}
