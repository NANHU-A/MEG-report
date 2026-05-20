import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    # 情景二：低煤价 + 高油价（研究框架下的近似梯队，从低到高）
    segments = [
        {
            "name": "一体化气头 +\n高效煤制",
            "width": 0.95,
            "cost": 18,
            "color": "#a8d08d",
            "cost_text": "18 美元/桶\n低成本供给",
        },
        {
            "name": "一体化油制\n中东/北美/中国沿海",
            "width": 0.60,
            "cost": 28,
            "color": "#9dc3e6",
            "cost_text": "22-30 美元/桶\n稳定供给",
        },
        {
            "name": "外采乙烯油制 +\n一般煤制",
            "width": 0.95,
            "cost": 46,
            "color": "#9e8cc5",
            "cost_text": "42-48 美元/桶\n边际供给",
        },
        {
            "name": "高成本出清区\n（油制为主）",
            "width": 0.70,
            "cost": 62,
            "color": "#ed7d31",
            "cost_text": "高成本出清\n（扩大）",
        },
        {
            "name": "高成本出清区\n（尾部）",
            "width": 0.55,
            "cost": 74,
            "color": "#c0504d",
            "cost_text": "出清尾部\n（扩大）",
        },
    ]

    widths = np.array([s["width"] for s in segments])
    lefts = np.cumsum(np.r_[0, widths[:-1]])
    mids = lefts + widths / 2
    total = float(widths.sum())

    # 4K级别（16:9）
    fig = plt.figure(figsize=(16, 9), dpi=240)
    fig.patch.set_facecolor("#d8e4c7")

    ax = fig.add_axes([0.06, 0.18, 0.88, 0.62])
    ax.set_facecolor("#d8e4c7")
    ax.set_xlim(0, total + 0.10)
    ax.set_ylim(0, 85)

    # 标题区（按参考风格，但置顶居中）
    fig.text(
        0.50,
        0.94,
        "全球供给：边际成本梯度曲线",
        fontsize=30,
        fontweight="bold",
        color="#111111",
        ha="center",
    )
    fig.text(
        0.50,
        0.905,
        "情景二 - 低煤价 + 高油价环境（研究框架）",
        fontsize=14.5,
        color="#333333",
        ha="center",
    )

    # 分位标记（位置按情景调整）
    p80 = total * 0.82
    p90 = total * 0.92
    ax.axvline(p80, color="#ff3333", linestyle="--", linewidth=1.2)
    ax.axvline(p90, color="#ff3333", linestyle="--", linewidth=1.2)
    ax.text(p80, 82.5, "80%分位\n边际成本", fontsize=14, ha="center", va="bottom", color="#111111")
    ax.text(p90, 82.5, "90%分位\n边际成本", fontsize=14, ha="center", va="bottom", color="#111111")

    # 组合式阶梯块
    for i, s in enumerate(segments):
        ax.add_patch(
            Rectangle(
                (lefts[i], 0),
                s["width"],
                s["cost"],
                facecolor=s["color"],
                edgecolor="#355c7d",
                linewidth=1.1,
            )
        )
        ax.text(
            mids[i],
            s["cost"] + 2.0,
            s["name"],
            ha="center",
            va="bottom",
            fontsize=12.0,
            color="#1a1a1a",
        )
        ax.text(
            mids[i],
            s["cost"] - 3.0,
            s["cost_text"],
            ha="center",
            va="top",
            fontsize=11.0,
            color="#1a1a1a",
        )

    # 累计边际成本曲线
    x_curve = np.r_[0, lefts[1:], total]
    y_curve = np.r_[segments[0]["cost"] - 1, [s["cost"] for s in segments[1:]], segments[-1]["cost"] + 2]
    ax.plot(x_curve, y_curve, color="#4f81bd", linewidth=2.6, marker="o", markersize=4.8)

    # 坐标轴样式
    ax.set_title("全球EG工艺路线边际成本梯队（情景二｜研究框架）", fontsize=18, pad=10)
    ax.set_xlabel("累计产能（相对尺度）", fontsize=12)
    ax.set_ylabel("边际成本（相对值）", fontsize=12)
    ax.grid(axis="y", color="#9ea99a", alpha=0.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
    ax.set_xticks([0, total * 0.25, total * 0.5, total * 0.75, total])
    ax.set_xticklabels(["0", "1", "2", "3", "4"], fontsize=11)

    # 图例（参考风格）
    legend = [
        Line2D([0], [0], color="#a8d08d", lw=10, label="一体化气头/高效煤制"),
        Line2D([0], [0], color="#9dc3e6", lw=10, label="一体化油制"),
        Line2D([0], [0], color="#9e8cc5", lw=10, label="外采乙烯油制/一般煤制"),
        Line2D([0], [0], color="#c0504d", lw=10, label="高成本出清"),
    ]
    ax.legend(handles=legend, loc="lower left", frameon=False, fontsize=11, ncol=2)

    fig.text(
        0.06,
        0.065,
        "EG边际成本是动态变化的，产能出清通常表现为‘转产—降负—退出’的渐进过程",
        fontsize=12.0,
        color="#222222",
    )
    fig.text(0.06, 0.03, "情景二：低煤价 + 高油价", fontsize=12.0, color="#222222")
    fig.text(
        0.50,
        0.03,
        "数据来源：CCF（2025聚酯产业市场年度报告）、卓创资讯、百川盈孚（2025-2026数据整理）",
        ha="center",
        fontsize=10.8,
        color="#222222",
    )
    fig.text(0.95, 0.03, "CIEC", ha="right", fontsize=22, fontweight="bold", color="#555")

    fig.savefig(
        "results/pictures/eg-marginal-cost-curve-scenario2-lowcoal-highoil.png",
        dpi=240,
        bbox_inches="tight",
    )
    fig.savefig("results/pictures/eg-marginal-cost-curve-scenario2-lowcoal-highoil.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
