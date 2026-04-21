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
    # 口径说明：以已确认的图片信息 + 公共公开文本整理，部分值为公开口径/估算
    rows = [
        ["聚酯总量", "8972", "+5.1%", "7984", "+6.88%"],
        ["涤纶长丝", "5491", "+4.1%", "—", "—"],
        ["涤纶短纤", "1004", "+5.6%", "882", "+8.9%"],
        ["瓶片", "2147", "+5.1%", "1605(YTD)", "+13.0%(YTD)"],
        ["切片(PET)", "878", "+3.5%", "—", "—"],
        ["薄膜(BOPET)", "680", "+3.0%", "—", "—"],
    ]

    cap_growth = np.array([5.1, 4.1, 5.6, 5.1, 3.5, 3.0])
    out_growth = np.array([6.88, np.nan, 8.9, 13.0, np.nan, np.nan])
    labels = ["总量", "长丝", "短纤", "瓶片", "切片", "薄膜"]
    x = np.arange(len(labels))

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

    # 左侧：增速对比图
    ax = fig.add_axes([0.06, 0.33, 0.54, 0.43], facecolor="none")
    ax2 = ax.twinx()
    width = 0.34

    cap_bars = ax.bar(
        x - width / 2,
        cap_growth,
        width,
        color="#3d66ad",
        label="产能增速（%）",
        zorder=3,
    )
    out_line = ax2.plot(
        x,
        out_growth,
        color="#ec7c2d",
        marker="o",
        lw=2.8,
        ms=6.5,
        label="产量增速（%）",
        zorder=4,
    )

    for i, v in enumerate(cap_growth):
        ax.text(
            i - width / 2,
            v + 0.18,
            f"{v:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color="#1f2a3a",
        )

    for i, v in enumerate(out_growth):
        if np.isnan(v):
            continue
        ax2.text(
            i,
            v + 0.25,
            f"{v:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color="#7a3f00",
        )

    ax.set_title("聚酯及下游细分产品增速对比", fontsize=21, pad=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11.5)
    ax.set_ylim(0, 7.2)
    ax.set_ylabel("产能增速（%）", fontsize=11.5)
    ax.grid(axis="y", color="#d0d0d0", lw=1.0, alpha=0.8)
    ax.set_axisbelow(True)

    ax2.set_ylim(0, 14.5)
    ax2.set_ylabel("产量增速（%）", fontsize=11.5)

    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
        ax2.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)
    ax2.tick_params(axis="both", length=0)

    handles = [
        Line2D([0], [0], color="#3d66ad", lw=8),
        Line2D([0], [0], color="#ec7c2d", lw=3, marker="o", markersize=6),
    ]
    labels_legend = ["产能增速（左轴）", "产量增速（右轴）"]
    ax.legend(
        handles,
        labels_legend,
        loc="lower center",
        bbox_to_anchor=(0.49, -0.20),
        ncol=2,
        frameon=False,
        fontsize=10.5,
    )

    # 右侧：表格
    ax_tbl = fig.add_axes([0.63, 0.25, 0.33, 0.57], facecolor="none")
    ax_tbl.set_axis_off()
    ax_tbl.set_title("2025年聚酯及五个细分的产能/产量增速表", fontsize=18, pad=10)

    table = ax_tbl.table(
        cellText=rows,
        colLabels=["品种", "2025产能", "产能增速", "2025产量", "产量增速"],
        cellLoc="center",
        colLoc="center",
        loc="center",
        bbox=[0.0, 0.08, 1.0, 0.82],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10.2)

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
        0.02,
        0.01,
        "注：切片=PET fiber chip；瓶片数据为公开可读口径，部分产量采用YTD或留空。",
        fontsize=9.5,
        color="#444",
        transform=ax_tbl.transAxes,
    )

    # 底部结论区，避开主图和表格，减少重叠
    fig.text(
        0.06,
        0.15,
        "结论：2025年聚酯总量维持增长，但细分分化更明显。",
        fontsize=14.5,
        color="#111",
    )
    fig.text(
        0.06,
        0.11,
        "- 短纤、瓶片增速高于总量，偏强；长丝与切片偏稳；薄膜增速相对最慢。",
        fontsize=13.5,
        color="#111",
    )
    fig.text(
        0.06,
        0.075,
        "- 公开文本未完整披露的品种，以‘—’标注，避免过度推断。",
        fontsize=13.5,
        color="#111",
    )

    fig.text(
        0.50,
        0.02,
        "数据来源：CCF 2025年报图片信息 + 公开行业资料整理（部分为估算口径）",
        ha="center",
        fontsize=12.5,
        color="#222",
    )
    fig.text(0.97, 0.02, "32", ha="right", fontsize=26, color="#222")

    plt.savefig("results/pictures/polyester_2025_comparison.png", dpi=170, bbox_inches="tight")
    plt.savefig("results/pictures/polyester_2025_comparison.svg", bbox_inches="tight")
    print("Polyester comparison charts saved successfully.")


if __name__ == "__main__":
    main()
