import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyBboxPatch


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    # ---- 情景二：低煤价 + 高油价 ----
    # coal routes shift LEFT (cheaper), oil routes shift RIGHT (more expensive)
    segments = [
        {
            "name": "一体化气头\n中东/北美/中国",
            "width": 0.75,
            "cost": 18,
            "color": "#c6e8b4",
            "sub": "低煤价下煤制成本大幅下降\n成为重要低成本供给",
            "rep": "代表：中国高效煤制、中东/北美一体化气头",
        },
        {
            "name": "一体化油制\n中东/北美/中国沿海",
            "width": 0.55,
            "cost": 28,
            "color": "#b4d7f0",
            "sub": "22-30 美元/桶\n稳定供给",
            "rep": "",
        },
        {
            "name": "外采乙烯油制\n+ 一般煤制",
            "width": 0.65,
            "cost": 45,
            "color": "#b5a2d5",
            "sub": "42-48 美元/桶\n边际供给",
            "rep": "",
        },
        {
            "name": "高成本出清区\n显著扩大",
            "width": 0.55,
            "cost": 68,
            "color": "#e8925c",
            "sub": "中国老旧油制装置\n日韩园区油制\n部分低效煤制",
            "rep": "",
        },
    ]

    widths = np.array([s["width"] for s in segments])
    lefts = np.cumsum(np.r_[0, widths[:-1]])
    mids = lefts + widths / 2
    total = widths.sum()

    # ---- figure ----
    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#d8e4c7")

    ax = fig.add_axes([0.08, 0.18, 0.84, 0.62])
    ax.set_facecolor("#d8e4c7")
    ax.set_xlim(0, total + 0.15)
    ax.set_ylim(0, 85)

    # ---- title block ----
    fig.text(0.05, 0.92, "全球供给：边际成本梯度曲线", fontsize=28, fontweight="bold", color="#111111")
    fig.text(
        0.50, 0.935,
        "情景二 - 低煤价 + 高油价环境（研究框架）",
        fontsize=14, color="#c00000", ha="left", va="center",
    )

    # ---- percentile markers ----
    pct80 = total * 0.80  # 2.00
    pct90 = total * 0.90  # 2.25

    ax.axvline(pct80, color="#c00000", linestyle="--", linewidth=1.2)
    ax.axvline(pct90, color="#c00000", linestyle="--", linewidth=1.2)
    fig.text(0.705, 0.835, "80%  分位\n边际成本", fontsize=13, ha="center", color="#111111")
    fig.text(0.825, 0.835, "90%  分位\n边际成本", fontsize=13, ha="center", color="#111111")

    # ---- rectangle blocks ----
    for i, s in enumerate(segments):
        ax.add_patch(
            Rectangle(
                (lefts[i], 0), s["width"], s["cost"],
                facecolor=s["color"], edgecolor="#355c7d", linewidth=1.1,
            )
        )
        # segment name above block
        ax.text(mids[i], s["cost"] + 2.5, s["name"], ha="center", va="bottom",
                fontsize=11.5, color="#1a1a1a", linespacing=1.3)

        # cost + sub-label inside block
        inner_text = s["sub"]
        ax.text(mids[i], s["cost"] - 4.5, inner_text, ha="center", va="top",
                fontsize=10.5, color="#1a1a1a", linespacing=1.3)

        # rep line for seg 0
        if s["rep"]:
            ax.text(mids[i], s["cost"] + 9.5, s["rep"], ha="center", va="bottom",
                    fontsize=10, color="#555555", style="italic")

    # ---- cumulative curve line ----
    x_curve = np.r_[0, lefts[1:], total]
    y_curve = np.r_[segments[0]["cost"] - 1, [s["cost"] for s in segments[1:]], segments[-1]["cost"] + 2]
    ax.plot(x_curve, y_curve, color="#4f81bd", linewidth=2.0, marker="o", markersize=5)

    # ---- axis styling ----
    ax.set_title("全球EG工艺路线边际成本梯队（情景二）", fontsize=18, pad=10)
    ax.set_xlabel("累计产能（相对尺度）", fontsize=12)
    ax.set_ylabel("边际成本（美元/桶等效）", fontsize=12)
    ax.grid(axis="y", color="#9ea99a", alpha=0.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
    ax.set_xticks([0, total * 0.25, total * 0.5, total * 0.75, total])
    ax.set_xticklabels(["0", "0.6", "1.3", "1.9", "2.5"], fontsize=11)

    # ---- legend ----
    legend_handles = [
        Line2D([0], [0], color="#c6e8b4", lw=10, label="一体化气头 + 高效煤制"),
        Line2D([0], [0], color="#b4d7f0", lw=10, label="一体化油制"),
        Line2D([0], [0], color="#b5a2d5", lw=10, label="外采乙烯油制 + 一般煤制"),
        Line2D([0], [0], color="#e8925c", lw=10, label="高成本出清区"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=False, fontsize=11, ncol=1)

    # ---- RED ANNOTATION BOX (top right) ----
    red_box = FancyBboxPatch(
        (0.56, 0.785), 0.38, 0.095,
        boxstyle="round,pad=0.02,rounding_size=0.01",
        facecolor="#fff5f5", edgecolor="#c00000", linewidth=1.8,
        transform=fig.transFigure,
    )
    fig.patches.append(red_box)
    fig.text(
        0.575, 0.86,
        "低煤价 + 高油价情景下，煤制路线成本大幅左移，\n"
        "成为中低成本产能；油制（尤其是外采乙烯油制）\n"
        "成本相对右移，高成本油制装置更易进入出清区间。",
        fontsize=11.5, color="#c00000", ha="left", va="center",
        linespacing=1.55,
    )

    # ---- bottom annotations ----
    fig.text(
        0.05, 0.095,
        "气头/一体化油头路线通常处于低成本梯队；EG边际成本是动态变化的，产能出清通常表现为"
        ""转产—降负—退出"的渐进过程，而非简单停产。",
        fontsize=11.5, color="#222222",
    )
    fig.text(0.05, 0.055, "情景二：低煤价 + 高油价", fontsize=12, fontweight="bold", color="#444444")

    # ---- data source ----
    fig.text(
        0.05, 0.025,
        "数据来源：CCF（2025聚酯产业市场年度报告）、卓创资讯、百川盈孚（2025-2026数据整理）",
        fontsize=10, color="#888888",
    )

    # ---- CIEC watermark ----
    fig.text(0.94, 0.025, "CIEC", fontsize=22, fontweight="bold", color="#888888", ha="right")

    # ---- export ----
    fig.savefig("results/pictures/eg_marginal_cost_low_coal_high_oil.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg_marginal_cost_low_coal_high_oil.svg", bbox_inches="tight")
    print("saved: eg_marginal_cost_low_coal_high_oil.png / .svg")


if __name__ == "__main__":
    main()
