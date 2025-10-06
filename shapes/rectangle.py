from .base import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        try:
            self.length = float(length)
            self.width = float(width)
        except ValueError:
            raise ValueError("长度和宽度必须为数字")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("长度和宽度必须为正数")

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def parameters(self) -> dict:
        return {"length": self.length, "width": self.width}
