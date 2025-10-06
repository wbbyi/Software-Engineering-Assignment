import unittest
import tkinter as tk

from gui.main_window import ShapeApp

class TestShapeAppAll(unittest.TestCase):

    def setUp(self):
        # 创建真正的 Tk 主窗口
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = ShapeApp(self.root)

    def tearDown(self):
        # 测试完成后销毁 root
        self.root.destroy()

    def simulate_input(self, shape_name, params):
        """切换图形并填入参数"""
        self.app.shape_var.set(shape_name)
        self.app.update_fields()
        for label, entry in self.app.entries.items():
            if label in params:
                entry.delete(0, tk.END)
                entry.insert(0, str(params[label]))

    def check_result_contains(self, expected_texts):
        """检查结果文本中包含预期的文本"""
        result = self.app.result_label.cget("text")
        for text in expected_texts:
            self.assertIn(text, result)

    # ---------- 测试所有图形的合法输入 ----------
    def test_triangle_valid(self):
        self.simulate_input("三角形", {"边a": 3, "边b": 4, "边c": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 6.00", "周长: 12.00"])

    def test_rectangle_valid(self):
        self.simulate_input("矩形", {"长度": 4, "宽度": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 20.00", "周长: 18.00"])

    def test_square_valid(self):
        self.simulate_input("正方形", {"边长": 4})
        self.app.calculate()
        self.check_result_contains(["面积: 16.00", "周长: 16.00"])

    def test_circle_valid(self):
        self.simulate_input("圆形", {"半径": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 78.54", "周长: 31.42"])

    def test_parallelogram_valid(self):
        self.simulate_input("平行四边形", {"底边": 6, "高": 4, "边长": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 24.00", "周长: 22.00"])

    def test_rhombus_valid(self):
        self.simulate_input("菱形", {"对角线1": 6, "对角线2": 8, "边长": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 24.00", "周长: 20.00"])

    def test_trapezoid_valid(self):
        self.simulate_input("梯形", {"上底": 6, "下底": 10, "高": 4, "左边": 5, "右边": 5})
        self.app.calculate()
        self.check_result_contains(["面积: 32.00", "周长: 26.00"])

    def test_hexagon_valid(self):
        self.simulate_input("正六边形", {"边长": 6})
        self.app.calculate()
        self.check_result_contains(["面积: 93.53", "周长: 36.00"])

    # ---------- 测试异常输入 ----------
    def test_triangle_invalid_sides(self):
        self.simulate_input("三角形", {"边a": 1, "边b": 2, "边c": 3})
        self.app.calculate()
        self.assertIn("错误", self.app.result_label.cget("text"))

    def test_circle_invalid_radius(self):
        self.simulate_input("圆形", {"半径": -5})
        self.app.calculate()
        self.assertIn("错误", self.app.result_label.cget("text"))

    def test_rectangle_invalid(self):
        self.simulate_input("矩形", {"长度": -4, "宽度": 5})
        self.app.calculate()
        self.assertIn("错误", self.app.result_label.cget("text"))

    def test_square_invalid(self):
        self.simulate_input("正方形", {"边长": 0})
        self.app.calculate()
        self.assertIn("错误", self.app.result_label.cget("text"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
