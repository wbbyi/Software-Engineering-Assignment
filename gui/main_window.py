import tkinter as tk
from tkinter import ttk, messagebox
from shapes import *
from gui.plotter import draw_shape

class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图形计算器")
        self.root.geometry("500x400")   # 设置窗口大小
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # 图形映射
        self.shape_classes = {
            "三角形": Triangle,
            "矩形": Rectangle,
            "正方形": Square,
            "平行四边形": Parallelogram,
            "菱形": Rhombus,
            "梯形": Trapezoid,
            "正六边形": Hexagon,
            "圆形": Circle,
        }

        # 顶部选择区
        select_frame = ttk.Frame(root)
        select_frame.grid(row=0, column=0, columnspan=2, pady=20)
        ttk.Label(select_frame, text="选择图形:").pack(side="left", padx=5)
        self.shape_var = tk.StringVar()
        self.shape_menu = ttk.Combobox(select_frame, textvariable=self.shape_var, state="readonly")
        self.shape_menu["values"] = list(self.shape_classes.keys())
        self.shape_menu.current(0)
        self.shape_menu.pack(side="left", padx=5)
        self.shape_menu.bind("<<ComboboxSelected>>", self.update_fields)

        # 参数区
        self.param_frame = ttk.Frame(root)
        self.param_frame.grid(row=1, column=0, columnspan=2, pady=20)
        self.entries = {}
        self.param_translation = {}
        self.update_fields()

        # 结果显示
        self.result_label = ttk.Label(root, text="结果将在这里显示", font=("Arial", 12))
        self.result_label.grid(row=2, column=0, columnspan=2, pady=20)

        # 按钮区
        btn_frame = ttk.Frame(root)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        ttk.Button(btn_frame, text="计算", command=self.calculate, width=10).pack(side="left", padx=20)
        ttk.Button(btn_frame, text="绘制", command=self.plot, width=10).pack(side="left", padx=20)

    def update_fields(self, event=None):
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.entries.clear()
        self.param_translation.clear()

        shape = self.shape_var.get()
        fields = {
            "三角形": [("边a", "a"), ("边b", "b"), ("边c", "c")],
            "矩形": [("长度", "length"), ("宽度", "width")],
            "正方形": [("边长", "side")],
            "平行四边形": [("底边", "base"), ("高", "height"), ("边长", "side")],
            "菱形": [("对角线1", "d1"), ("对角线2", "d2"), ("边长", "side")],
            "梯形": [("上底", "base1"), ("下底", "base2"), ("高", "height"), ("左边", "side1"), ("右边", "side2")],
            "正六边形": [("边长", "side")],
            "圆形": [("半径", "radius")],
        }[shape]

        for i, (ch_name, en_name) in enumerate(fields):
            ttk.Label(self.param_frame, text=f"{ch_name}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(self.param_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.entries[ch_name] = entry
            self.param_translation[ch_name] = en_name

    def calculate(self):
        try:
            params = {self.param_translation[k]: float(v.get()) for k, v in self.entries.items()}
            shape_cls = self.shape_classes[self.shape_var.get()]
            shape = shape_cls(**params)
            area, peri = shape.area(), shape.perimeter()
            self.result_label.config(text=f"面积: {area:.2f}, 周长: {peri:.2f}")
        except Exception as e:
            # 将错误显示在 label 上，而不是弹窗
            self.result_label.config(text=f"错误: {str(e)}")

    def plot(self):
        try:
            params = {self.param_translation[k]: float(v.get()) for k, v in self.entries.items()}
            draw_shape(self.shape_var.get(), params)
        except Exception as e:
            messagebox.showerror("错误", str(e))
