import math
from .base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        # 边长必须大于 0
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("三角形边长必须大于 0")
        # 必须满足三角形不等式
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("三角形边长不满足三角形不等式")

        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def parameters(self) -> dict:
        return {"a": self.a, "b": self.b, "c": self.c}
