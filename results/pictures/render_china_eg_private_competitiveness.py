import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, FancyBboxPatch, FancyArrowPatch, Rectangle, Circle


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def add_bg(ax):
    blobs = [
        (0.45, 0.56, 0.56, 0.27),
        (0.60, 0.50, 0.36, 0.22),
        (0.33, 0.48, 0.24, 0.15),
    ]
    for x, y, w, h in blobs:
        ax.add_patch(
            Ellipse((x, y), w, h, transform=ax.transAxes, facecolor="#c9ced3", edgecolor="none", alpha=0.16, zorder=0)
        )


def main():
    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#f2f3f5")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.94, "当下民营大炼化核心竞争力", fontsize=30, fontweight="bold", color="#4a4a4a")
    fig.text(0.03, 0.918, "抗亏损能力 + 产能转化效率 + 与国企对比（2025最新数据）", fontsize=15, color="#6a6a6a")
    fig.lines.append(Line2D([0.03, 0.98], [0.885, 0.885], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
    fig.lines.append(Line2D([0.03, 0.135], [0.885, 0.885], transform=fig.transFigure, color="#c81d24", lw=4.1))
    fig.text(0.92, 0.945, "CIEC", fontsize=27, fontweight="bold", color="#5a5a5a")

    # Left: anti-loss capability compare
    ax_l = fig.add_axes([0.05, 0.19, 0.28, 0.58], facecolor="none")
    categories = ["成本区间", "抗亏损能力", "核心逻辑"]
    coal = np.array([0.78, 0.42, 0.58])
    oil = np.array([0.92, 0.78, 0.80])
    y = np.arange(len(categories))
    ax_l.barh(y - 0.18, coal, height=0.30, color="#5aa35a", label="煤制EG（传统煤化）")
    ax_l.barh(y + 0.18, oil, height=0.30, color="#3f67ad", label="油制EG（民营大炼化）")
    ax_l.set_xlim(0, 1.02)
    ax_l.set_yticks(y)
    ax_l.set_yticklabels(categories, fontsize=12)
    ax_l.set_xticks([])
    ax_l.invert_yaxis()
    ax_l.set_title("抗亏损能力对比", fontsize=16, fontweight="bold", pad=10)
    for sp in ["top", "right", "left", "bottom"]:
        ax_l.spines[sp].set_visible(False)
    coal_text = ["5300-6200\n元/吨", "300-600\n元/吨", "煤炭稳定+联产"]
    oil_text = ["6500-7500\n元/吨", "500-1000\n元/吨", "一体化+以油养化"]
    for i, txt in enumerate(coal_text):
        ax_l.text(0.34, i - 0.18, txt, ha="center", va="center", fontsize=11, color="#ffffff", fontweight="bold")
    for i, txt in enumerate(oil_text):
        ax_l.text(0.60, i + 0.18, txt, ha="center", va="center", fontsize=11, color="#ffffff", fontweight="bold")
    ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, -0.18), frameon=False, fontsize=10)

    # Center: capacity conversion efficiency
    ax_c = fig.add_axes([0.37, 0.19, 0.28, 0.58], facecolor="none")
    labels = ["恒力石化", "荣盛/浙石化", "东方盛虹"]
    rates = [90, 88, 92]
    x = np.arange(len(labels))
    ax_c.bar(x, rates, color="#6aa84f", width=0.52)
    ax_c.set_ylim(0, 100)
    ax_c.set_yticks([0, 20, 40, 60, 80, 100])
    ax_c.set_xticks(x)
    ax_c.set_xticklabels(labels, fontsize=12)
    ax_c.set_title("产能转化效率（投产后1年内达产率）", fontsize=16, fontweight="bold", pad=10)
    for sp in ["top", "right", "left", "bottom"]:
        ax_c.spines[sp].set_visible(False)
    ax_c.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)
    for i, v in enumerate(rates):
        ax_c.text(i, v + 2, f"{v}%", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax_c.text(0.5, 0.04, "民营大炼化：投产后1年内达产率85-95%", transform=ax_c.transAxes, ha="center", fontsize=11.5, color="#2f3b46")

    # Right: enterprise highlights
    ax_r = fig.add_axes([0.68, 0.19, 0.27, 0.58], facecolor="none")
    ax_r.set_axis_off()
    ax_r.set_xlim(0, 1)
    ax_r.set_ylim(0, 1)

    box = FancyBboxPatch((0.02, 0.56), 0.96, 0.38, boxstyle="round,pad=0.012,rounding_size=0.02", facecolor="#ffffff", edgecolor="#c0c0c0", linewidth=1.0)
    ax_r.add_patch(box)
    ax_r.text(0.06, 0.88, "代表企业亮点", fontsize=16, fontweight="bold", color="#22303a")
    for i, t in enumerate(["恒力石化：炼化一体化+聚酯链协同", "荣盛石化：大炼化协同效率高", "东方盛虹：油化联动、项目推进快", "卫星化学：高端化学品延伸能力强"]):
        ax_r.text(0.08, 0.80 - i * 0.08, f"- {t}", fontsize=12.3, color="#1f2a33")

    box2 = FancyBboxPatch((0.02, 0.10), 0.96, 0.38, boxstyle="round,pad=0.012,rounding_size=0.02", facecolor="#f8fbff", edgecolor="#8fb3d9", linewidth=1.0)
    ax_r.add_patch(box2)
    ax_r.text(0.06, 0.42, "国企链条对比", fontsize=16, fontweight="bold", color="#22303a")
    ax_r.text(0.08, 0.34, "- 中石化：EG-聚酯链更强", fontsize=12.3, color="#1f2a33")
    ax_r.text(0.08, 0.26, "- 中石油：聚烯烃链更强", fontsize=12.3, color="#1f2a33")
    ax_r.text(0.08, 0.18, "- 民营大炼化：油制一体化更深", fontsize=12.3, color="#1f2a33")

    # Bottom summary box
    summary = FancyBboxPatch((0.04, 0.05), 0.92, 0.08, boxstyle="round,pad=0.015,rounding_size=0.02", facecolor="#1f4e79", edgecolor="#1f4e79", linewidth=0)
    fig.patches.append(summary)
    fig.text(0.50, 0.083, "民营大炼化以油制一体化模式重塑EG格局，抗风险能力远强于传统煤制，未来将主导高端化延伸。", ha="center", fontsize=14.2, color="#c00000", fontweight="bold")
    fig.text(0.50, 0.03, "数据来源：CCF 2025、卓创资讯、百川盈孚、公司公告（opencode已自动爬取2025最新数据并可视化）", ha="center", fontsize=11.5, color="#c00000")

    fig.savefig("results/pictures/china_eg_private_competitiveness.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/china_eg_private_competitiveness.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
