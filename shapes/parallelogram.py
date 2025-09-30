from .base import Shape

class Parallelogram(Shape):
    def __init__(self, base: float, height: float, side: float):
        self.base, self.height, self.side = base, height, side

    def area(self) -> float:
        return self.base * self.height

    def perimeter(self) -> float:
        return 2 * (self.base + self.side)

    def parameters(self) -> dict:
        return {"base": self.base, "height": self.height, "side": self.side}
