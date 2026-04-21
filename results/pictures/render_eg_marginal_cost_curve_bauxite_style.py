import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyBboxPatch


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    # 研究框架下的近似梯队（从低到高）
    segments = [
        {"name": "一体化油制\n中东/北美/新加坡", "width": 0.40, "cost": 20, "color": "#d6e9c6", "label": "低成本基荷"},
        {"name": "园区油制\n韩国/台/日/中国沿海", "width": 0.55, "cost": 28, "color": "#a8d08d", "label": "稳定供给"},
        {"name": "外采乙烯油制\n中国/东南亚/印度/欧洲", "width": 0.65, "cost": 38, "color": "#5b9bd5", "label": "边际供给"},
        {"name": "高效煤制\n中国", "width": 0.75, "cost": 50, "color": "#9e8cc5", "label": "边际供给"},
        {"name": "一般煤制\n中国老旧装置", "width": 0.60, "cost": 62, "color": "#ed7d31", "label": "高成本出清"},
        {"name": "老旧/受限装置\n区域小装置", "width": 0.40, "cost": 74, "color": "#c0504d", "label": "高成本出清"},
    ]

    # cumulative x axis
    widths = np.array([s["width"] for s in segments])
    lefts = np.cumsum(np.r_[0, widths[:-1]])
    mids = lefts + widths / 2
    total = widths.sum()

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#d8e4c7")

    ax = fig.add_axes([0.08, 0.15, 0.82, 0.68])
    ax.set_facecolor("#d8e4c7")
    ax.set_xlim(0, total + 0.10)
    ax.set_ylim(0, 85)

    # Title and annotations
    fig.text(0.05, 0.90, "全球EG供应端边际成本曲线", fontsize=28, fontweight="bold", color="#111111")
    fig.text(0.57, 0.91, "边际成本动态移动：乙烯、煤、电价格波动会改变梯队位置", fontsize=14.5, color="#c00000")
    fig.text(0.73, 0.84, "80%分位\n边际成本", fontsize=14, ha="center", color="#111111")
    fig.text(0.85, 0.84, "90%分位\n边际成本", fontsize=14, ha="center", color="#111111")

    # percentile markers
    ax.axvline(total * 0.84, color="#ff3333", linestyle="--", linewidth=1.2)
    ax.axvline(total * 0.94, color="#ff3333", linestyle="--", linewidth=1.2)

    # blocks
    for i, s in enumerate(segments):
        ax.add_patch(Rectangle((lefts[i], 0), s["width"], s["cost"], facecolor=s["color"], edgecolor="#355c7d", linewidth=1.1))
        ax.text(mids[i], s["cost"] + 2.0, s["name"], ha="center", va="bottom", fontsize=11.5, color="#1a1a1a")
        ax.text(mids[i], s["cost"] - 3.0, f"{s['cost']} 美元/桶\n{ s['label'] }", ha="center", va="top", fontsize=10.5, color="#1a1a1a")

    # cumulative curve
    x_curve = np.r_[0, lefts[1:], total]
    y_curve = np.r_[segments[0]["cost"] - 1, [s["cost"] for s in segments[1:]], segments[-1]["cost"] + 2]
    ax.plot(x_curve, y_curve, color="#4f81bd", linewidth=2.0, marker="o", markersize=4)

    # axis style
    ax.set_title("全球EG工艺路线边际成本梯队（研究框架）", fontsize=18, pad=10)
    ax.set_xlabel("累计产能（相对尺度）", fontsize=12)
    ax.set_ylabel("边际成本（相对值）", fontsize=12)
    ax.grid(axis="y", color="#9ea99a", alpha=0.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
    ax.set_xticks([0, total * 0.25, total * 0.5, total * 0.75, total])
    ax.set_xticklabels(["0", "0.5", "1.5", "2.5", "4"], fontsize=11)

    # right side note box
    note = FancyBboxPatch((total * 0.64, 66), total * 0.32, 15, boxstyle="round,pad=0.012,rounding_size=0.012", facecolor="#f6f6f6", edgecolor="#777", linewidth=1.0)
    ax.add_patch(note)
    ax.text(total * 0.65, 78, "中国煤制是全球重要\n但偏高成本的边际供给", fontsize=12.5, color="#c00000")
    ax.text(total * 0.65, 70.5, "外采乙烯油制与低效率煤制\n在下跌周期最先减产", fontsize=11.5, color="#111")

    # legend
    legend = [
        Line2D([0], [0], color="#d6e9c6", lw=10, label="一体化油制"),
        Line2D([0], [0], color="#5b9bd5", lw=10, label="外采乙烯油制"),
        Line2D([0], [0], color="#9e8cc5", lw=10, label="煤制"),
        Line2D([0], [0], color="#c0504d", lw=10, label="高成本出清"),
    ]
    ax.legend(handles=legend, loc="lower left", frameon=False, fontsize=11, ncol=2)

    fig.text(0.05, 0.06, "注：边际成本为动态概念，受乙烯、煤价、电价、装置效率及一体化程度影响；图中为研究框架下的近似梯队。", fontsize=11.5, color="#222")
    fig.text(0.90, 0.06, "CIEC", fontsize=20, fontweight="bold", color="#555")

    fig.savefig("results/pictures/eg-marginal-cost-curve-bauxite-style.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg-marginal-cost-curve-bauxite-style.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
