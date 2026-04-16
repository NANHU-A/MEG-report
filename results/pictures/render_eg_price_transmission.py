import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch


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
                alpha=0.22,
                zorder=0,
            )
        )


def draw_box(ax, x, y, w, h, title, lines, fc="#f7f7f7", ec="#7f8c9a"):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.02",
        linewidth=1.6,
        edgecolor=ec,
        facecolor=fc,
        zorder=2,
    )
    ax.add_patch(box)
    ax.text(
        x + 0.015,
        y + h - 0.04,
        title,
        fontsize=16,
        fontweight="bold",
        color="#2f3b46",
        zorder=3,
    )
    y0 = y + h - 0.08
    for line in lines:
        ax.text(x + 0.018, y0, line, fontsize=12.5, color="#1f2a33", zorder=3)
        y0 -= 0.042


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

    ax = fig.add_axes([0.04, 0.08, 0.92, 0.79])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    draw_box(
        ax,
        0.02,
        0.56,
        0.30,
        0.34,
        "1. 刚性单耗（需求端）",
        [
            "- 1吨PET = 0.335吨MEG + 0.855吨PTA",
            "- PET扩产对MEG边际需求：",
            "  新增PET产能 x 0.335",
            "- 结论：PET扩产直接抬升MEG刚性需求",
        ],
        fc="#f5f9ff",
        ec="#4f81bd",
    )

    draw_box(
        ax,
        0.35,
        0.56,
        0.30,
        0.34,
        "2. 成本驱动链条（供给端）",
        [
            "油制：原油 -> 石脑油 -> 乙烯 -> MEG",
            "- 油价每变动10美元/桶，MEG成本变动500-600元/吨",
            "煤制：煤炭 -> 合成气 -> MEG",
            "- 原料煤占成本51%，电力+蒸汽占16%",
            "- 煤价每变动100元/吨，MEG成本变动约50元/吨",
        ],
        fc="#fff8f2",
        ec="#ed7d31",
    )

    draw_box(
        ax,
        0.68,
        0.56,
        0.30,
        0.34,
        "3. 替代效应（生产端）",
        [
            "- MEG高度同质化，下游无法区分来源",
            "- 替代本质：能源比价驱动开工率此消彼长",
            "- 油价80-90美元/桶：煤制较油制优势1500-2000元/吨",
            "- 高油价：煤制开工率上升，油制降负",
            "- 低油价：油制修复，煤制优势收窄",
        ],
        fc="#f4fff4",
        ec="#70ad47",
    )

    arr_kw = dict(
        arrowstyle="-|>", mutation_scale=16, linewidth=2.0, color="#6b6f74", alpha=0.9
    )
    ax.add_patch(FancyArrowPatch((0.325, 0.73), (0.345, 0.73), **arr_kw))
    ax.add_patch(FancyArrowPatch((0.655, 0.73), (0.675, 0.73), **arr_kw))

    draw_box(
        ax,
        0.18,
        0.17,
        0.64,
        0.28,
        "前瞻信号与交易跟踪",
        [
            "- 核心跟踪：煤制与油制开工率背离",
            "- 信号解释：开工率差距扩大 => 替代效应兑现加速",
            "- 价格传导路径：PET扩产(需求) + 能源成本(供给) + 开工率切换(替代)",
            "  共同决定MEG价格弹性与利润分配",
        ],
        fc="#f8f8f8",
        ec="#7f7f7f",
    )

    ax.add_patch(
        FancyArrowPatch(
            (0.50, 0.56),
            (0.50, 0.46),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=2.0,
            color="#6b6f74",
            alpha=0.9,
        )
    )

    fig.text(
        0.50,
        0.02,
        "数据来源：用户给定逻辑框架整理；参数为产业研究常用估算口径（更新至2025）",
        ha="center",
        fontsize=13,
        color="#4f4f4f",
    )

    fig.savefig(
        "results/pictures/eg-price-transmission.png", dpi=170, bbox_inches="tight"
    )
    fig.savefig("results/pictures/eg-price-transmission.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
