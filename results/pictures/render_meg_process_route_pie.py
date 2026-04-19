import matplotlib.pyplot as plt
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
        (0.45, 0.57, 0.55, 0.25),
        (0.58, 0.50, 0.36, 0.22),
        (0.34, 0.49, 0.24, 0.15),
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
    # 根据用户给定信息，取中值口径：其他路线按7%（5-10%区间中值）
    labels = ["油头（石脑油）", "气头（乙烷）", "煤头（煤基）", "其他路线"]
    sizes = [50, 26, 17, 7]
    colors = ["#3f67ad", "#ed7d31", "#70ad47", "#a5a5a5"]

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(
        0.03,
        0.94,
        "全球MEG工艺路线产能结构",
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
            [0.03, 0.13],
            [0.90, 0.90],
            transform=fig.transFigure,
            color="#c81d24",
            lw=4.1,
        )
    )
    fig.text(0.92, 0.945, "CIEC", fontsize=28, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.40, 0.18, 0.40, 0.62], facecolor="none")
    wedges, _texts, _autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        autopct=lambda p: f"{p:.0f}%",
        pctdistance=0.70,
        wedgeprops={"linewidth": 2, "edgecolor": "white"},
        textprops={"fontsize": 14, "color": "#1f2a33"},
    )
    ax.set_aspect("equal")

    ax.legend(
        wedges,
        labels,
        loc="center left",
        bbox_to_anchor=(0.98, 0.5),
        frameon=False,
        fontsize=13,
    )

    fig.text(0.05, 0.64, "结构解读", fontsize=22, fontweight="bold", color="#2f3b46")
    fig.text(
        0.05, 0.56, "- 油头约50%，主要在东北亚与欧洲", fontsize=17, color="#1f2a33"
    )
    fig.text(
        0.05,
        0.49,
        "- 气头约26%，集中中东和北美，成本优势突出",
        fontsize=17,
        color="#1f2a33",
    )
    fig.text(0.05, 0.42, "- 煤头约17%，高度集中在中国", fontsize=17, color="#1f2a33")
    fig.text(
        0.05,
        0.35,
        "- 其他路线约7%（混烷轻烃制/MTO/乙烯单体制等）",
        fontsize=17,
        color="#1f2a33",
    )
    fig.text(
        0.05, 0.26, "注：中国境内煤头约占中国总产能40%", fontsize=17, color="#1f2a33"
    )

    fig.text(
        0.50,
        0.02,
        "数据来源：用户给定口径整理；其他路线取5-10%区间中值估算",
        ha="center",
        fontsize=13,
        color="#555555",
    )

    fig.savefig(
        "results/pictures/meg-process-route-pie.png", dpi=170, bbox_inches="tight"
    )
    fig.savefig("results/pictures/meg-process-route-pie.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
