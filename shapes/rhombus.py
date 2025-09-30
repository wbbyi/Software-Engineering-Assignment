from .base import Shape

class Rhombus(Shape):
    def __init__(self, d1: float, d2: float, side: float):
        self.d1, self.d2, self.side = d1, d2, side

    def area(self) -> float:
        return (self.d1 * self.d2) / 2

    def perimeter(self) -> float:
        return 4 * self.side

    def parameters(self) -> dict:
        return {"d1": self.d1, "d2": self.d2, "side": self.side}
