import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse


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
                alpha=0.18,
                zorder=0,
            )
        )


def main():
    years = np.array([2021, 2022, 2023, 2024, 2025])
    capacity = np.array([2049.5, 2477.5, 2792.5, 2857.5, 2903.0])
    output = np.array([1237.0, 1368.7, 1678.0, 1960.0, 2100.0])
    import_ratio = np.array([40.8, 35.5, 30.0, 25.2, 27.0])

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.94, "中国MEG生产消费情况（2021-2025）", fontsize=30, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
    fig.lines.append(Line2D([0.03, 0.14], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.2))
    fig.text(0.92, 0.945, "CIEC", fontsize=27, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.08, 0.22, 0.80, 0.56], facecolor="none")
    ax2 = ax.twinx()
    x = np.arange(len(years))

    ax.bar(x, capacity, width=0.48, color="#3f67ad", edgecolor="none", label="MEG产能（万吨）", zorder=2)
    ax.plot(x, output, color="#ed7d31", linewidth=3.0, marker="o", markersize=7, label="MEG产量（万吨）", zorder=3)

    for i, v in enumerate(capacity):
        ax.text(i, v + 45, f"{v:.1f}".rstrip("0").rstrip("."), ha="center", va="bottom", fontsize=10.5, color="#1e2e4b")
    for i, v in enumerate(output):
        ax.text(i, v + 35, f"{v:.1f}".rstrip("0").rstrip("."), ha="center", va="bottom", fontsize=10.5, color="#7a3f00")

    ax.set_xlim(-0.5, len(years) - 0.5)
    ax.set_ylim(0, 3300)
    ax.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000])
    ax.set_ylabel("万吨", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{y}年" for y in years], fontsize=12)
    ax.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)
    ax.set_axisbelow(True)
    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)

    ax2.set_ylim(0, 50)
    ax2.set_yticks([0, 10, 20, 30, 40, 50])
    ax2.set_ylabel("进口依存度（%）", fontsize=13)
    ax2.plot(x, import_ratio, color="#70ad47", linewidth=2.8, marker="s", markersize=6, label="进口依存度（右轴）", zorder=3)
    for i, v in enumerate(import_ratio):
        ax2.text(i, v + 1.0, f"{v:.1f}%".rstrip("0").rstrip("."), ha="center", va="bottom", fontsize=10.0, color="#385723")
    for sp in ["top", "right", "left", "bottom"]:
        ax2.spines[sp].set_visible(False)
    ax2.tick_params(axis="both", length=0)

    handles = [
        Line2D([0], [0], color="#3f67ad", lw=8),
        Line2D([0], [0], color="#ed7d31", lw=3, marker="o", markersize=6),
        Line2D([0], [0], color="#70ad47", lw=3, marker="s", markersize=6),
    ]
    labels = ["产能（万吨，左轴）", "产量（万吨，左轴）", "进口依存度（右轴）"]
    ax.legend(handles, labels, loc="upper left", frameon=False, fontsize=12)

    fig.text(0.08, 0.14, "- 中国MEG产能持续扩张，2025年达到2903万吨。", fontsize=16, color="#1f2a33")
    fig.text(0.08, 0.10, "- 产量从2021年1237万吨增长至2025年2100万吨。", fontsize=16, color="#1f2a33")
    fig.text(0.08, 0.06, "- 进口依存度由40.8%降至25.2%，2025年回升至27.0%。", fontsize=16, color="#1f2a33")

    fig.text(0.50, 0.02, "数据来源：公开行业资料整理（2021-2025，估算口径）", ha="center", fontsize=13, color="#555555")

    fig.savefig("results/pictures/eg-china-capacity-output-2021-2025-ppt.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg-china-capacity-output-2021-2025-ppt.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
