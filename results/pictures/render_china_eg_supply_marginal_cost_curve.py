import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

def main():
    segments = [
        {"name": "民营大炼化\n一体化油制", "width": 0.40, "cost": 30, "color": "#d6e9c6", "label": "最低成本基荷"},
        {"name": "高效煤制\n", "width": 0.30, "cost": 42, "color": "#5b9bd5", "label": "主力支撑"},
        {"name": "外采乙烯油制\n一般煤制", "width": 0.20, "cost": 55, "color": "#9e8cc5", "label": "边际供给"},
        {"name": "小型/非一体化煤制\n老旧/短流程油制", "width": 0.10, "cost": 72, "color": "#ed7d31", "label": "最易出清"},
    ]

    widths = np.array([s["width"] for s in segments])
    lefts = np.cumsum(np.r_[0, widths[:-1]])
    mids = lefts + widths / 2
    total = widths.sum()

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#d8e4c7")

    ax = fig.add_axes([0.08, 0.15, 0.82, 0.68])
    ax.set_facecolor("#d8e4c7")
    ax.set_xlim(0, total + 0.05)
    ax.set_ylim(0, 85)

    # Title and annotations
    fig.text(0.05, 0.90, "中国EG供应端边际成本曲线", fontsize=28, fontweight="bold", color="#111111")
    fig.text(0.57, 0.91, "边际成本动态移动：乙烯、煤、电价格波动会改变梯队位置", fontsize=14.5, color="#c00000")
    fig.text(0.73, 0.84, "80%分位\n边际成本", fontsize=14, ha="center", color="#111111")
    fig.text(0.85, 0.84, "90%分位\n边际成本", fontsize=14, ha="center", color="#111111")

    # percentile markers
    ax.axvline(total * 0.80, color="#ff3333", linestyle="--", linewidth=1.2)
    ax.axvline(total * 0.90, color="#ff3333", linestyle="--", linewidth=1.2)

    # blocks
    for i, s in enumerate(segments):
        ax.add_patch(Rectangle((lefts[i], 0), s["width"], s["cost"], facecolor=s["color"], edgecolor="#355c7d", linewidth=1.1))
        ax.text(mids[i], s["cost"] + 2.0, s["name"], ha="center", va="bottom", fontsize=11.5, color="#1a1a1a")
        # Approximate dynamic costs
        ax.text(mids[i], s["cost"] - 3.0, f"{ s['label'] }", ha="center", va="top", fontsize=11.5, color="#1a1a1a")

    # cumulative curve
    x_curve = np.r_[0, lefts[1:], total]
    y_curve = np.r_[segments[0]["cost"] - 1, [s["cost"] for s in segments[1:]], segments[-1]["cost"] + 2]
    ax.plot(x_curve, y_curve, color="#4f81bd", linewidth=2.0, marker="o", markersize=4)

    # axis style
    ax.set_title("中国EG工艺路线边际成本梯队（2025研究框架）", fontsize=18, pad=10)
    ax.set_xlabel("累计产能（相对尺度）", fontsize=12)
    ax.set_ylabel("边际成本（相对值）", fontsize=12)
    ax.grid(axis="y", color="#9ea99a", alpha=0.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.set_yticks([0, 20, 40, 60, 80])
    ax.set_xticks([0, total * 0.25, total * 0.5, total * 0.75, total])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"], fontsize=11)

    # legend
    legend = [
        Line2D([0], [0], color="#d6e9c6", lw=10, label="一体化油制"),
        Line2D([0], [0], color="#5b9bd5", lw=10, label="高效煤制"),
        Line2D([0], [0], color="#9e8cc5", lw=10, label="外采/一般煤制"),
        Line2D([0], [0], color="#ed7d31", lw=10, label="老旧/边缘产能"),
    ]
    ax.legend(handles=legend, loc="lower left", frameon=False, fontsize=11, ncol=2)

    fig.text(0.05, 0.06, "注：边际成本为动态概念，受乙烯、煤价、电价等波动影响；此为2025研究框架下的近似梯队而非绝对装置成本。", fontsize=11.5, color="#222")
    fig.text(0.90, 0.06, "研究框架", fontsize=16, fontweight="bold", color="#555")

    os.makedirs("results/pictures", exist_ok=True)
    fig.savefig("results/pictures/china_eg_supply_marginal_cost_curve.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/china_eg_supply_marginal_cost_curve.svg", bbox_inches="tight")
    print("saved")

if __name__ == "__main__":
    main()
