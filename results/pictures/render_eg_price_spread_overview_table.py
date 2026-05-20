import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def add_bg(ax):
    for x, y, w, h in [
        (0.44, 0.56, 0.54, 0.27),
        (0.59, 0.50, 0.35, 0.21),
        (0.34, 0.48, 0.24, 0.15),
        (0.72, 0.44, 0.22, 0.13),
    ]:
        ax.add_patch(
            Ellipse(
                (x, y), w, h, transform=ax.transAxes, facecolor="#c9ced3", edgecolor="none", alpha=0.18, zorder=0
            )
        )


def main():
    rows = [
        ["盘面价格", "期货合约价格", "对未来供需、库存和交割预期的综合定价", "市场对远期均衡的判断"],
        ["基差", "现货价-期货价", "现货松紧与盘面共同作用", "现货强弱、交割压力、套保价值"],
        ["月差", "近月-远月", "未来供需、库存变化及交割预期", "期限结构、去库/累库预期"],
        ["区域价差", "不同区域现货价差", "区域供需失衡、库存分布与物流约束", "区域紧张度、货物流向与套利空间"],
        ["品种价差", "同品类内部价差", "标品/非标、品牌、仓单及交割属性差异", "品质分层、流通偏好与交割溢价"],
    ]

    fig = plt.figure(figsize=(16, 10), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.945, "EG：价格、价差、库存与物流的关系总领", fontsize=28, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.905, 0.905], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
    fig.lines.append(Line2D([0.03, 0.12], [0.905, 0.905], transform=fig.transFigure, color="#c81d24", lw=4.2))
    fig.text(0.92, 0.95, "CIEC", fontsize=28, fontweight="bold", color="#5a5a5a")
    fig.text(
        0.04,
        0.865,
        "供需错配先传导至库存，再通过现货、盘面、区域与品种价差形成信号；物流在满足价差覆盖成本时发生，并反向修正库存与价差。",
        fontsize=12.5,
        color="#c81d24",
    )

    ax = fig.add_axes([0.03, 0.10, 0.94, 0.72])
    ax.set_axis_off()

    table = ax.table(
        cellText=rows,
        colLabels=["价格信号/价差类型", "核心定义", "形成机制（本质）", "主要反映什么"],
        cellLoc="left",
        colLoc="center",
        loc="center",
        bbox=[0.0, 0.04, 1.0, 0.91],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(18.0)

    widths = {0: 0.16, 1: 0.17, 2: 0.36, 3: 0.31}
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#d2d2d2")
        cell.set_linewidth(0.8)
        cell.set_width(widths.get(c, 0.25))
        cell.set_height(0.125 if r == 0 else 0.105)
        if r == 0:
            cell.set_facecolor("#d9e2f3")
            cell.set_text_props(weight="bold", color="#1f2a3a", ha="center")
        else:
            cell.set_facecolor("#ffffff" if r % 2 == 0 else "#f7f9fc")
            if c == 0:
                cell.set_text_props(weight="bold", color="#1f2a3a")
            else:
                cell.set_text_props(color="#222")

    fig.text(0.50, 0.025, "注：‘品种价差’仅指同一品类内部差异；跨品种比较请单列为联动价差。", ha="center", fontsize=11.8, color="#444")
    fig.text(0.97, 0.02, "68", ha="right", fontsize=26, color="#222")

    fig.savefig("results/pictures/eg_price_spread_overview_table.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg_price_spread_overview_table.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
