from .base import Shape

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length, self.width = length, width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def parameters(self) -> dict:
        return {"length": self.length, "width": self.width}
