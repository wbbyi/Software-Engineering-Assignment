from .base import Shape

class Trapezoid(Shape):
    def __init__(self, base1: float, base2: float, side1: float, side2: float, height: float):
        (self.base1, self.base2, self.side1,
         self.side2, self.height) = base1, base2, side1, side2, height

    def area(self) -> float:
        return (self.base1 + self.base2) * self.height / 2

    def perimeter(self) -> float:
        return self.base1 + self.base2 + self.side1 + self.side2

    def parameters(self) -> dict:
        return {"base1": self.base1, "base2": self.base2,
                "side1": self.side1, "side2": self.side2,
                "height": self.height}
