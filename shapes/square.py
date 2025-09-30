from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)  # 正方形长宽相等
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"
