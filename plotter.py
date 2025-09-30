import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle as pltCircle
import math

def draw_shape(name: str, params: dict):
    fig, ax = plt.subplots(figsize=(6, 6))  # 画布大小
    shape = None

    if name == "三角形":
        a, b, c = params["a"], params["b"], params["c"]

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("给定的边长无法构成三角形")

        sides = [('a', a), ('b', b), ('c', c)]
        sides.sort(key=lambda x: x[1], reverse=True)
        a_name, a_val = sides[0]  # 最长边
        b_name, b_val = sides[1]
        c_name, c_val = sides[2]

        a, b, c = a_val, b_val, c_val
        x1, y1 = 0, 0
        x2, y2 = c, 0

        cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
        cosA = max(-1, min(1, cosA))

        x3 = b * cosA
        y3 = math.sqrt(max(0, b ** 2 - x3 ** 2))

        shape = Polygon(
            [[x1, y1], [x2, y2], [x3, y3]],
            closed=True,
            facecolor="orange",
            edgecolor="red",
            alpha=0.6
        )
        ax.add_patch(shape)


    elif name == "矩形":
        l, w = params["length"], params["width"]
        shape = Polygon(
            [[0, 0], [l, 0], [l, w], [0, w]],
            closed=True,
            facecolor="lightblue",
            edgecolor="blue",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "正方形":
        s = params["side"]
        shape = Polygon(
            [[0, 0], [s, 0], [s, s], [0, s]],
            closed=True,
            facecolor="pink",
            edgecolor="purple",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "平行四边形":
        b, h = params["base"], params["height"]
        offset = params.get("offset", b / 3)
        shape = Polygon(
            [[0, 0], [b, 0], [b + offset, h], [offset, h]],
            closed=True,
            facecolor="lightyellow",
            edgecolor="gold",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "菱形":
        d1, d2 = params["d1"], params["d2"]
        shape = Polygon(
            [[0, d2/2], [d1/2, 0], [0, -d2/2], [-d1/2, 0]],
            closed=True,
            facecolor="lightgreen",
            edgecolor="green",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "梯形":
        b1, b2, h = params["base1"], params["base2"], params["height"]

        if b1 < b2:
            b1, b2 = b2, b1

        offset = (b1 - b2) / 2
        shape = Polygon(
            [[0, 0], [b1, 0], [b1 - offset, h], [offset, h]],
            closed=True,
            facecolor="violet",
            edgecolor="purple",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "正六边形":
        s = params["side"]
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = s * math.cos(angle)
            y = s * math.sin(angle)
            points.append((x, y))
        shape = Polygon(
            points,
            closed=True,
            facecolor="skyblue",
            edgecolor="navy",
            alpha=0.6
        )
        ax.add_patch(shape)

    elif name == "圆形":
        r = params["radius"]
        shape = pltCircle(
            (0, 0),
            r,
            facecolor="lightcoral",
            edgecolor="red",
            alpha=0.6
        )
        ax.add_patch(shape)

    # 中文支持
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    ax.set_aspect("equal")
    ax.autoscale_view()
    plt.title(name)
    plt.show()
