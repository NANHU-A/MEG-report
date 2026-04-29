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
                alpha=0.35,
                zorder=0,
            )
        )


def fmt(v, digits=1):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "—"
    if isinstance(v, str):
        return v
    return f"{v:.{digits}f}"


def main():
    # 口径说明：按用户指定地区合并——河南并入华北，华中+西南合并
    rows = [
        ["西北", "0", "100%", "0"],
        ["华北(含河南)", "16.9%", "83.1%", "0"],
        ["华南", "91.3%", "8.7%", "0"],
        ["华东", "87.5%", "7.7%", "4.8%"],
        ["东北", "100%", "0", "0"],
        ["华中+西南", "23.4%", "76.6%", "0"],
    ]

    col_labels = ["地区", "石脑油制", "合成气制", "MTO制"]

    fig = plt.figure(figsize=(16, 9), dpi=160)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_world_like_bg(bg)

    fig.text(
        0.03,
        0.94,
        "3.2.1 2025年聚酯产品产能产量增速对比",
        fontsize=28,
        fontweight="bold",
        color="#4a4a4a",
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
    fig.text(0.92, 0.945, "CIEC", fontsize=28, fontweight="bold", color="#5a5a5a")

    # 右侧：表格
    ax_tbl = fig.add_axes([0.05, 0.31, 0.90, 0.45], facecolor="none")
    ax_tbl.set_axis_off()
    ax_tbl.set_title("各地区工艺占比（河南并入华北，华中+西南合并）", fontsize=20, pad=10)

    table = ax_tbl.table(
        cellText=rows,
        colLabels=col_labels,
        cellLoc="center",
        colLoc="center",
        loc="center",
        bbox=[0.0, 0.02, 1.0, 0.88],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(11.5)

    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#d2d2d2")
        cell.set_linewidth(0.8)
        if r == 0:
            cell.set_facecolor("#d9e2f3")
            cell.set_text_props(weight="bold", color="#1f2a3a")
        elif r % 2 == 1:
            cell.set_facecolor("#f5f7fa")
        else:
            cell.set_facecolor("#ffffff")

    ax_tbl.text(
        0.01,
        -0.10,
        "注：石脑油制=SD/Shell/Dow/BASF/UCC；MTO制含 MTO, SHELL氧化法；其余无对应装置记0。",
        fontsize=9.8,
        color="#444",
        transform=ax_tbl.transAxes,
    )

    fig.text(
        0.06,
        0.12,
        "结论：石脑油制为主体，合成气制在西北/华北（含河南）/华中+西南占比较高，华东同时保有少量MTO。",
        fontsize=14,
        color="#111",
    )
    fig.text(
        0.06,
        0.08,
        "- 河南并入华北后，华北合成气制占比明显抬升；华中+西南整体以合成气制为主。",
        fontsize=13,
        color="#111",
    )

    fig.text(
        0.50,
        0.02,
        "数据来源：用户提供图片 + 工艺口径对应表整理（按地区合并口径）",
        ha="center",
        fontsize=12.5,
        color="#222",
    )
    fig.text(0.97, 0.02, "55", ha="right", fontsize=26, color="#222")

    plt.savefig("results/pictures/polyester_2025_comparison.png", dpi=170, bbox_inches="tight")
    plt.savefig("results/pictures/polyester_2025_comparison.svg", bbox_inches="tight")
    print("Polyester comparison charts saved successfully.")


if __name__ == "__main__":
    main()
