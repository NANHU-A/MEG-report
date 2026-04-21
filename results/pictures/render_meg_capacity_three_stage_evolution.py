import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, FancyBboxPatch


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
            Ellipse(
                (x, y),
                w,
                h,
                transform=ax.transAxes,
                facecolor="#c9ced3",
                edgecolor="none",
                alpha=0.16,
                zorder=0,
            )
        )


def main():
    # 2018-2025 historical, 2026-2030 forecast (万吨)
    years = np.arange(2018, 2031)
    capacity = np.array([760, 1070, 1570, 2049.5, 2477.5, 2792.5, 2984.0, 3174.0, 3190, 3210, 3230, 3250, 3270])
    output = np.array([500, 650, 822, 1237.0, 1368.7, 1678.0, 1849.0, 2016.1, 2050, 2080, 2120, 2160, 2200])

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#f2f3f5")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.94, "中国EG行业主流投产方式演变", fontsize=30, fontweight="bold", color="#4a4a4a")
    fig.text(0.03, 0.926, "过去 · 现在 · 未来（基于2025最新数据）", fontsize=15, color="#6a6a6a")
    fig.lines.append(Line2D([0.03, 0.98], [0.885, 0.885], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
    fig.lines.append(Line2D([0.03, 0.13], [0.885, 0.885], transform=fig.transFigure, color="#c81d24", lw=4.1))
    fig.text(0.92, 0.945, "CIEC", fontsize=27, fontweight="bold", color="#5a5a5a")

    # Main chart
    ax = fig.add_axes([0.06, 0.18, 0.61, 0.63], facecolor="none")
    ax2 = ax.twinx()
    x = np.arange(len(years))

    # stage shading
    ax.axvspan(-0.5, 6.5, color="#dce9f6", alpha=0.42, zorder=0)   # 2018-2024
    ax.axvspan(6.5, 7.5, color="#dff1df", alpha=0.50, zorder=0)    # 2025
    ax.axvspan(7.5, 12.5, color="#f8e7d9", alpha=0.45, zorder=0)   # 2026-2030

    # capacity bars: historical solid, future hatched/transparent
    hist_end = 8  # 2018-2025 inclusive
    ax.bar(x[:hist_end], capacity[:hist_end], width=0.55, color="#3f67ad", edgecolor="none", zorder=2, label="MEG产能（左轴）")
    ax.bar(x[hist_end-1:], capacity[hist_end-1:], width=0.55, color="#3f67ad", edgecolor="#3f67ad", alpha=0.28, hatch="//", linewidth=1.0, zorder=2)

    # output line: historical solid, forecast dashed
    ax.plot(x[:hist_end], output[:hist_end], color="#ed7d31", linewidth=3.0, marker="o", markersize=6.5, zorder=3, label="MEG产量（左轴）")
    ax.plot(x[hist_end-1:], output[hist_end-1:], color="#ed7d31", linewidth=2.6, linestyle="--", marker="o", markersize=6.5, zorder=3)

    # 2025 pivot highlight
    ax.axvline(7, color="#68a357", linewidth=1.4, linestyle="--", alpha=0.9)
    ax.text(7, 3200, "2025", ha="center", va="bottom", fontsize=12, color="#3f6f35", fontweight="bold")

    # Labels
    key_years = {0, 2, 3, 6, 7, 12}
    for i, v in enumerate(capacity):
        if i in key_years or i >= 7:
            ax.text(i, v + 40, f"{v:.0f}" if float(v).is_integer() else f"{v:.1f}", ha="center", va="bottom", fontsize=9.8, color="#1e2e4b")
    for i, v in enumerate(output):
        if i in key_years or i >= 7:
            offset = 26 if i % 2 == 0 else -38
            ax.text(i, v + offset, f"{v:.0f}" if float(v).is_integer() else f"{v:.1f}", ha="center", va="center", fontsize=9.4, color="#7a3f00")

    # axis
    ax.set_xlim(-0.5, len(years) - 0.5)
    ax.set_ylim(0, 3500)
    ax.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
    ax.set_ylabel("万吨", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{y}年" for y in years], fontsize=10)
    ax.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)
    ax.set_axisbelow(True)
    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)

    ax2.set_ylim(0, 100)
    ax2.set_yticks([0, 20, 40, 60, 80, 100])
    ax2.set_ylabel("进口依存度（%）", fontsize=13)
    import_ratio = np.array([54.0, 49.5, 44.0, 40.8, 35.5, 30.0, 25.2, 27.0, 26.4, 26.0, 25.8, 25.5, 25.0])
    ax2.plot(x, import_ratio, color="#70ad47", linewidth=2.4, marker="s", markersize=5.5, zorder=3, label="进口依存度（右轴）")
    for i in [0, 3, 7, 12]:
        ax2.text(i, import_ratio[i] + 1.0, f"{import_ratio[i]:.1f}%", ha="center", va="bottom", fontsize=9.2, color="#385723")
    for sp in ["top", "right", "left", "bottom"]:
        ax2.spines[sp].set_visible(False)
    ax2.tick_params(axis="both", length=0)

    # Stage separators + labels above chart
    ax.text(2.5, 3470, "过去（2018-2024）\n煤制爆发式扩张", ha="center", va="top", fontsize=13.5, color="#335b88", fontweight="bold")
    ax.text(7.0, 3470, "现在（2022-2025）\n民营大炼化一体化成为主流", ha="center", va="top", fontsize=13.5, color="#2f6d3f", fontweight="bold")
    ax.text(10.5, 3470, "未来（2026-2030）\n新增放缓，转向存量优化", ha="center", va="top", fontsize=13.5, color="#9a5c20", fontweight="bold")

    # Legend
    handles = [
        Line2D([0], [0], color="#3f67ad", lw=8),
        Line2D([0], [0], color="#ed7d31", lw=3, marker="o", markersize=6),
        Line2D([0], [0], color="#70ad47", lw=2.4, marker="s", markersize=5.5),
    ]
    labels = ["产能（万吨）", "产量（万吨）", "进口依存度（%）"]
    ax.legend(handles, labels, loc="upper left", frameon=False, fontsize=11)

    # Right annotation panel
    panel = FancyBboxPatch((0.70, 0.22), 0.26, 0.58, boxstyle="round,pad=0.014,rounding_size=0.018", facecolor="#ffffff", edgecolor="#b3b3b3", linewidth=1.0, transform=fig.transFigure)
    fig.patches.append(panel)
    fig.text(0.715, 0.765, "三阶段投产逻辑", fontsize=18, fontweight="bold", color="#22303a")
    fig.text(0.715, 0.705, "1. 过去：煤制集中投产\n原因：煤化工技术突破+资源禀赋\n结果：产能快速上行，成为供给主增量。", fontsize=11.8, color="#1f2a33")
    fig.text(0.715, 0.565, "2. 现在：民营大炼化/油制上量\n原因：炼化一体化、园区协同、下游配套\n结果：乙烯制占比抬升，新增煤制明显放缓。", fontsize=11.8, color="#1f2a33")
    fig.text(0.715, 0.425, "3. 未来：新增放缓、重心转向优化\n原因：行业进入尾声、盈利分化与环保约束\n结果：更多存量优化与高端延伸。", fontsize=11.8, color="#1f2a33")
    fig.text(0.715, 0.315, "关键词：民营大炼化深化  |  煤制谨慎  |  存量优化", fontsize=11.0, color="#9a5c20")

    # bottom notes
    fig.text(0.06, 0.12, "- 2018-2024为扩产主周期，2025接近产能高位；2026-2030为放缓与优化阶段。", fontsize=14.0, color="#1f2a33")
    fig.text(0.06, 0.08, "- 产能/产量左轴，进口依存度右轴；虚线段为2026-2030预测。", fontsize=14.0, color="#1f2a33")
    fig.text(0.50, 0.02, "数据来源：华经、观研、168tex与公开行业资料整理（2021-2025为实数锚点，2018-2020及2026-2030为研究估算）", ha="center", fontsize=11.5, color="#555555")

    fig.savefig("results/pictures/eg-capacity-output-three-stage-evolution.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg-capacity-output-three-stage-evolution.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
