from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float):
        # 可以选择在这里单独验证
        if side <= 0:
            raise ValueError("边长必须为正数")
        super().__init__(side, side)  # 调用 Rectangle 构造函数

    def __str__(self):
        return f"Square(side={self.length})"  # length == width == side

    def parameters(self):
        return {"side": self.length}
