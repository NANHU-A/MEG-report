import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Circle


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def add_world_like_bg(ax):
    blobs = [
        (0.45, 0.56, 0.56, 0.28),
        (0.59, 0.50, 0.36, 0.21),
        (0.34, 0.48, 0.25, 0.16),
        (0.72, 0.44, 0.22, 0.13),
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


def box(ax, x, y, w, h, title, lines, fc, ec):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.02",
        facecolor=fc,
        edgecolor=ec,
        linewidth=1.8,
        zorder=2,
    )
    ax.add_patch(p)
    ax.text(
        x + 0.02,
        y + h - 0.05,
        title,
        fontsize=15,
        fontweight="bold",
        color="#2f3b46",
        zorder=3,
    )
    yy = y + h - 0.10
    for t in lines:
        ax.text(x + 0.02, yy, t, fontsize=12.5, color="#1f2a33", zorder=3)
        yy -= 0.046


def main():
    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_world_like_bg(bg)

    fig.text(
        0.03,
        0.94,
        "4.X 产业链：价格传导（MEG）",
        fontsize=31,
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
            [0.03, 0.135],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#c81d24",
            lw=4.2,
        )
    )
    fig.text(0.92, 0.945, "CIEC", fontsize=28, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.04, 0.09, 0.92, 0.78])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    box(
        ax,
        0.03,
        0.57,
        0.28,
        0.30,
        "刚性单耗（需求锚）",
        [
            "- 1吨PET = 0.335吨MEG + 0.855吨PTA",
            "- MEG边际需求 = 新增PET产能 x 0.335",
            "- PET扩产直接抬升MEG刚性需求",
        ],
        "#f5f9ff",
        "#4f81bd",
    )

    box(
        ax,
        0.36,
        0.57,
        0.28,
        0.30,
        "成本驱动（供给锚）",
        [
            "- 油制：10美元/桶 -> 500-600元/吨",
            "- 煤制：100元/吨煤 -> 50元/吨MEG",
            "- 煤占成本51%，电汽占16%",
        ],
        "#fff8f2",
        "#ed7d31",
    )

    box(
        ax,
        0.69,
        0.57,
        0.28,
        0.30,
        "替代效应（开工锚）",
        [
            "- 下游难区分来源，替代发生在生产端",
            "- 油价80-90美元/桶：煤制优势1500-2000元/吨",
            "- 高油价煤制升、低油价油制升",
        ],
        "#f4fff4",
        "#70ad47",
    )

    # Center MEG node
    center = Circle(
        (0.50, 0.36),
        0.08,
        facecolor="#3f67ad",
        edgecolor="#2e4f87",
        linewidth=2.0,
        zorder=4,
    )
    ax.add_patch(center)
    ax.text(
        0.50,
        0.38,
        "MEG",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color="white",
        zorder=5,
    )
    ax.text(
        0.50,
        0.33,
        "价格中枢",
        ha="center",
        va="center",
        fontsize=12.5,
        color="white",
        zorder=5,
    )

    # Flow arrows to center
    arr = dict(
        arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color="#6b6f74", alpha=0.92
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.17, 0.57), (0.43, 0.40), connectionstyle="arc3,rad=-0.08", **arr
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.50, 0.57), (0.50, 0.45), connectionstyle="arc3,rad=0.0", **arr
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.83, 0.57), (0.57, 0.40), connectionstyle="arc3,rad=0.08", **arr
        )
    )

    box(
        ax,
        0.18,
        0.08,
        0.64,
        0.20,
        "前瞻信号（可跟踪）",
        [
            "- 重点监控：煤制开工率 vs 油制开工率",
            "- 开工率差扩大 => 替代效应兑现 => MEG价格弹性上升",
            "- 建议结合PET投产节奏与油煤比价联动判断",
        ],
        "#f8f8f8",
        "#7f7f7f",
    )
    ax.add_patch(
        FancyArrowPatch(
            (0.50, 0.28),
            (0.50, 0.20),
            arrowstyle="-|>",
            mutation_scale=18,
            linewidth=2.2,
            color="#6b6f74",
            alpha=0.92,
        )
    )

    fig.text(
        0.50,
        0.018,
        "数据来源：用户给定逻辑框架整理；参数为产业研究常用估算口径（更新至2025）",
        ha="center",
        fontsize=13,
        color="#4f4f4f",
    )

    fig.savefig(
        "results/pictures/eg-price-transmission-diagram.png",
        dpi=170,
        bbox_inches="tight",
    )
    fig.savefig(
        "results/pictures/eg-price-transmission-diagram.svg", bbox_inches="tight"
    )
    print("saved")


if __name__ == "__main__":
    main()
