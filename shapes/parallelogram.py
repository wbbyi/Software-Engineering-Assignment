from .base import Shape

class Parallelogram(Shape):
    def __init__(self, base: float, height: float, side: float):
        try:
            base = float(base)
            height = float(height)
            side = float(side)
        except ValueError:
            raise ValueError("底边、高、侧边必须为数字")

        if base <= 0 or height <= 0 or side <= 0:
            raise ValueError("底边、高、侧边必须为正数")

        self.base = base
        self.height = height
        self.side = side


    def area(self) -> float:
        return self.base * self.height

    def perimeter(self) -> float:
        return 2 * (self.base + self.side)

    def parameters(self) -> dict:
        return {"base": self.base, "height": self.height, "side": self.side}
