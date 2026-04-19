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


def add_world_like_bg(ax):
    blobs = [
        (0.43, 0.53, 0.50, 0.25),
        (0.57, 0.52, 0.36, 0.22),
        (0.70, 0.45, 0.28, 0.16),
        (0.33, 0.48, 0.22, 0.14),
    ]
    for x, y, w, h in blobs:
        ax.add_patch(
            Ellipse(
                (x, y),
                w,
                h,
                transform=ax.transAxes,
                facecolor="#cbd1d8",
                edgecolor="none",
                alpha=0.45,
                zorder=0,
            )
        )


def main():
    years = np.arange(2021, 2026)
    # 中国MEG供给（估算口径，万吨），与参考图趋势大致对齐
    domestic = np.array([1230, 1360, 1680, 1930, 2080])
    imports = np.array([840, 760, 730, 670, 790])
    total_supply = imports + domestic
    import_ratio = imports / total_supply * 100

    fig = plt.figure(figsize=(16, 9), dpi=160)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_world_like_bg(bg)

    fig.text(
        0.03, 0.94, "4.1.1 中国供给：", fontsize=30, fontweight="bold", color="#4a4a4a"
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.98],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#4a4a4a",
            lw=2.5,
        )
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.115],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#c81d24",
            lw=4.0,
        )
    )
    fig.text(0.92, 0.945, "CIEC", fontsize=30, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.06, 0.31, 0.54, 0.41], facecolor="none")
    ax2 = ax.twinx()
    x = np.arange(len(years))

    ax.bar(
        x,
        imports,
        width=0.42,
        color="#3d66ad",
        edgecolor="none",
        label="进口量（左轴）",
        zorder=3,
    )
    ax.bar(
        x,
        domestic,
        bottom=imports,
        width=0.42,
        color="#69a83a",
        edgecolor="none",
        label="自产量（左轴）",
        zorder=3,
    )

    ax2.plot(
        x, import_ratio, color="#ec7c2d", lw=3.0, label="进口依存度（右轴）", zorder=4
    )

    for i, v in enumerate(imports):
        ax.text(
            i,
            v * 0.52,
            f"{v:.1f}",
            ha="center",
            va="center",
            fontsize=10,
            color="#1f2a3a",
        )
    for i, v in enumerate(domestic):
        ax.text(
            i,
            imports[i] + v * 0.50,
            f"{v:.1f}",
            ha="center",
            va="center",
            fontsize=10,
            color="#26401a",
        )

    ax.set_title("中国MEG总供给（万吨）", fontsize=24, pad=14)
    ax.set_xlim(-0.5, len(years) - 0.5)
    ax.set_ylim(0, 3200)
    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=90, fontsize=10)
    ax.set_yticks([0, 800, 1600, 2400, 3200])
    ax.tick_params(axis="y", labelsize=11)
    ax.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)

    ax2.set_ylim(0, 100)
    ax2.set_yticks([0, 20, 40, 60, 80, 100])
    ax2.tick_params(axis="y", labelsize=11)

    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
    for sp in ["top", "right", "left", "bottom"]:
        ax2.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)
    ax.tick_params(axis="x", pad=1)
    ax2.tick_params(axis="both", length=0)

    handles = [
        Line2D([0], [0], color="#3d66ad", lw=6),
        Line2D([0], [0], color="#69a83a", lw=6),
        Line2D([0], [0], color="#ec7c2d", lw=3),
    ]
    labels = ["进口量（左轴）", "自产量（左轴）", "进口依存度（右轴）"]
    ax.legend(
        handles,
        labels,
        loc="lower center",
        bbox_to_anchor=(0.46, -0.20),
        ncol=3,
        frameon=False,
        fontsize=10,
    )

    ax_pie = fig.add_axes([0.65, 0.27, 0.30, 0.43], facecolor="none")
    share_import = imports[-1] / total_supply[-1] * 100
    share_domestic = domestic[-1] / total_supply[-1] * 100

    wedges, _ = ax_pie.pie(
        [share_import, share_domestic],
        colors=["#3d66ad", "#69a83a"],
        startangle=90,
        counterclock=False,
        wedgeprops={"linewidth": 2, "edgecolor": "#f0f0f0"},
    )
    ax_pie.set_aspect("equal")
    ax_pie.set_title("2025年中国MEG供给结构", fontsize=20, pad=14)
    for label, pct, w in [
        ("进口", share_import, wedges[0]),
        ("自产", share_domestic, wedges[1]),
    ]:
        ang = (w.theta1 + w.theta2) / 2.0
        r = 0.56
        x_t = r * np.cos(np.deg2rad(ang))
        y_t = r * np.sin(np.deg2rad(ang))
        ax_pie.text(
            x_t,
            y_t,
            f"{label},\n{pct:.1f}%",
            ha="center",
            va="center",
            fontsize=15,
            color="#111111",
        )

    fig.text(
        0.17,
        0.105,
        "-  2021-2024年进口依存度明显下行，2025年随需求恢复小幅回升至约27.5%",
        fontsize=18,
        color="#111",
    )
    fig.text(
        0.17,
        0.055,
        "-  一体化与煤制路线投产推动国产供给提升，进口增量节奏放缓",
        fontsize=18,
        color="#111",
    )

    fig.text(
        0.50,
        0.006,
        "数据来源：公开行业资料整理（2021-2025，估算口径）",
        ha="center",
        fontsize=14,
        color="#222",
    )
    fig.text(0.97, 0.02, "22", ha="right", fontsize=28, color="#222")

    fig.savefig(
        "results/pictures/meg-china-supply-template.png", dpi=170, bbox_inches="tight"
    )
    fig.savefig("results/pictures/meg-china-supply-template.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
