import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def add_bg(ax):
    blobs = [
        (0.46, 0.56, 0.56, 0.27),
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
                alpha=0.20,
                zorder=0,
            )
        )


def main():
    # 单位：万吨（2019-2025，基于公开资料与锚点估算整理）
    years = np.arange(2019, 2026)
    capacity = np.array([1070, 1210, 1500, 1950, 2460, 2984, 3180])
    output = np.array([760, 822, 1006, 1232, 1508, 1849, 2060])

    cagr_2020_2024 = (output[5] / output[1]) ** (1 / 4) - 1

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(
        0.03,
        0.94,
        "4.X 中国供给：MEG产能与产量（2019-2025）",
        fontsize=30,
        fontweight="bold",
        color="#4a4a4a",
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.98],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#4a4a4a",
            lw=2.4,
        )
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.125],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#c81d24",
            lw=4.1,
        )
    )
    fig.text(0.92, 0.945, "CIEC", fontsize=28, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.08, 0.24, 0.78, 0.55], facecolor="none")
    x = np.arange(len(years))

    bars = ax.bar(
        x, capacity, width=0.55, color="#3f67ad", edgecolor="none", alpha=0.95, zorder=2
    )
    ax.plot(
        x, output, color="#ed7d31", linewidth=3.0, marker="o", markersize=7, zorder=3
    )

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=12)
    ax.set_ylim(0, 3500)
    ax.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
    ax.set_ylabel("万吨", fontsize=13)
    ax.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)
    ax.set_axisbelow(True)

    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="both", length=0)

    # 全点位数据标注（柱状+折线）
    for i, v in enumerate(capacity):
        ax.text(
            i,
            v + 70,
            f"{int(v)}",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color="#1e2e4b",
        )

    for i, v in enumerate(output):
        ax.text(
            i,
            v + 45,
            f"{int(v)}",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color="#7a3f00",
        )

    # 图例
    handles = [
        Line2D([0], [0], color="#3f67ad", lw=8),
        Line2D([0], [0], color="#ed7d31", lw=3, marker="o", markersize=6),
    ]
    labels = ["产能（万吨，柱）", "产量（万吨，折线）"]
    ax.legend(handles, labels, loc="upper left", frameon=False, fontsize=12)

    fig.text(
        0.08,
        0.14,
        "- 中国是过去五年全球MEG产能增长核心引擎：2019年约1070万吨 -> 2024年约2984万吨。",
        fontsize=16,
        color="#1f2a33",
    )
    fig.text(
        0.08,
        0.10,
        f"- 产量从2020年822万吨增至2024年1849万吨，对应年复合增长率约{cagr_2020_2024 * 100:.1f}%。",
        fontsize=16,
        color="#1f2a33",
    )
    fig.text(
        0.08,
        0.06,
        "- 2025年延续扩产放量趋势（估算口径）：产能约3180万吨，产量约2060万吨。",
        fontsize=16,
        color="#1f2a33",
    )

    fig.text(
        0.50,
        0.02,
        "数据来源：公开行业资料与网络检索整理（2019-2025，部分为估算口径）",
        ha="center",
        fontsize=13,
        color="#555555",
    )

    fig.savefig(
        "results/pictures/eg-china-capacity-output-2019-2025.png",
        dpi=170,
        bbox_inches="tight",
    )
    fig.savefig(
        "results/pictures/eg-china-capacity-output-2019-2025.svg", bbox_inches="tight"
    )
    print("saved")


if __name__ == "__main__":
    main()
