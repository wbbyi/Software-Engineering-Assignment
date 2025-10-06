from .base import Shape

class Rhombus(Shape):
    def __init__(self, d1, d2, side):
        try:
            self.d1 = float(d1)
            self.d2 = float(d2)
            self.side = float(side)
        except ValueError:
            raise ValueError("对角线和边长必须为数字")

        if self.d1 <= 0 or self.d2 <= 0 or self.side <= 0:
            raise ValueError("对角线和边长必须为正数")

    def area(self) -> float:
        return (self.d1 * self.d2) / 2

    def perimeter(self) -> float:
        return 4 * self.side

    def parameters(self) -> dict:
        return {"d1": self.d1, "d2": self.d2, "side": self.side}
