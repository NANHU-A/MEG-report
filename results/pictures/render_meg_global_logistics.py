import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Polygon


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def draw_world_map(ax, face="#dee4eb", edge="#f7f9fb", lw=1.1, alpha=1.0, z=1):
    continents = [
        [
            (0.05, 0.55),
            (0.12, 0.70),
            (0.20, 0.72),
            (0.26, 0.62),
            (0.23, 0.50),
            (0.16, 0.45),
            (0.09, 0.48),
        ],
        [
            (0.20, 0.42),
            (0.24, 0.36),
            (0.27, 0.24),
            (0.25, 0.12),
            (0.20, 0.07),
            (0.15, 0.12),
            (0.16, 0.24),
        ],
        [
            (0.36, 0.66),
            (0.42, 0.71),
            (0.48, 0.68),
            (0.47, 0.60),
            (0.42, 0.56),
            (0.37, 0.58),
        ],
        [
            (0.44, 0.54),
            (0.50, 0.50),
            (0.54, 0.40),
            (0.52, 0.22),
            (0.48, 0.10),
            (0.42, 0.18),
            (0.40, 0.34),
        ],
        [
            (0.54, 0.58),
            (0.62, 0.62),
            (0.69, 0.58),
            (0.76, 0.62),
            (0.85, 0.58),
            (0.88, 0.50),
            (0.82, 0.46),
            (0.74, 0.46),
            (0.67, 0.40),
            (0.60, 0.43),
            (0.55, 0.50),
        ],
        [(0.66, 0.34), (0.71, 0.33), (0.74, 0.28), (0.70, 0.20), (0.64, 0.23)],
        [
            (0.81, 0.20),
            (0.88, 0.18),
            (0.92, 0.12),
            (0.89, 0.06),
            (0.82, 0.08),
            (0.78, 0.14),
        ],
    ]
    for pts in continents:
        ax.add_patch(
            Polygon(
                pts,
                closed=True,
                facecolor=face,
                edgecolor=edge,
                linewidth=lw,
                alpha=alpha,
                zorder=z,
            )
        )


def add_trade_tag(ax, x, y, name, importer, exporter, dx=0.0, dy=0.0):
    # 模板式双段标签：左深色(Importer) + 中灰色 + 右黄色(Exporter)
    w1, w2, w3 = 0.10, 0.055, 0.06
    h = 0.045

    x0 = x + dx - (w1 + w2 + w3) / 2
    y0 = y + dy

    ax.text(
        x0 + w1 / 2,
        y0,
        name,
        ha="center",
        va="center",
        fontsize=8,
        color="white",
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.24,rounding_size=0.95",
            facecolor="#7f6f6d",
            edgecolor="none",
        ),
        zorder=6,
    )
    ax.text(
        x0 + w1 + w2 / 2,
        y0,
        f"{importer}",
        ha="center",
        va="center",
        fontsize=8,
        color="#f5f6f7",
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.24,rounding_size=0.35",
            facecolor="#aca57e",
            edgecolor="none",
        ),
        zorder=6,
    )
    ax.text(
        x0 + w1 + w2 + w3 / 2,
        y0,
        f"{exporter}",
        ha="center",
        va="center",
        fontsize=8,
        color="#6e5600",
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.24,rounding_size=0.95",
            facecolor="#f3bd3e",
            edgecolor="none",
        ),
        zorder=6,
    )

    ax.plot([x, x], [y + 0.01, y0 - 0.018], color="#616161", lw=0.9, zorder=4)
    ax.scatter([x], [y], s=10, color="#555555", zorder=5)


def main():
    # 单位：万吨；缺口 = 产量 - 消费量（负值=净进口）
    raw = [
        [2020, 735, 831, -96, 114, 130, -16, 276, 268, 8],
        [2021, 768, 876, -108, 118, 135, -17, 280, 271, 9],
        [2022, 794, 905, -111, 120, 139, -19, 287, 280, 7],
        [2023, 812, 934, -122, 122, 143, -21, 291, 286, 5],
        [2024, 830, 961, -131, 124, 146, -22, 296, 292, 4],
        [2025, 852, 994, -142, 126, 150, -24, 301, 298, 3],
    ]

    cagr_text = ["3.0%", "2.9%", "1.7%"]

    table_rows = [
        [
            "万吨",
            "亚太",
            "",
            "",
            "",
            "美洲",
            "",
            "",
            "",
            "欧洲、中东及非洲",
            "",
            "",
            "",
        ],
        [
            "年份",
            "产量",
            "消费量",
            "缺口",
            "复合增速",
            "产量",
            "消费量",
            "缺口",
            "复合增速",
            "产量",
            "消费量",
            "缺口",
            "复合增速",
        ],
    ]
    for y, ap_p, ap_c, ap_g, am_p, am_c, am_g, emea_p, emea_c, emea_g in raw:
        table_rows.append(
            [
                str(y),
                f"{ap_p:.0f}",
                f"{ap_c:.0f}",
                f"{ap_g:.0f}",
                "",
                f"{am_p:.0f}",
                f"{am_c:.0f}",
                f"{am_g:.0f}",
                "",
                f"{emea_p:.0f}",
                f"{emea_c:.0f}",
                f"{emea_g:.0f}",
                "",
            ]
        )

    anchors = {
        "北美": (0.17, 0.60),
        "南美": (0.21, 0.22),
        "西欧": (0.43, 0.60),
        "非洲": (0.47, 0.34),
        "中东": (0.57, 0.49),
        "南亚": (0.66, 0.41),
        "东北亚": (0.78, 0.57),
        "东南亚": (0.72, 0.30),
    }

    # 2025 粗量级流向（单位：万吨）
    flows = [
        ("中东", "东北亚", 320, 0.12),
        ("中东", "南亚", 190, -0.10),
        ("中东", "东南亚", 170, -0.20),
        ("中东", "西欧", 95, 0.05),
        ("中东", "非洲", 70, -0.27),
        ("北美", "东北亚", 165, 0.16),
        ("北美", "西欧", 85, 0.09),
        ("北美", "南美", 55, -0.13),
        ("东北亚", "南亚", 45, -0.25),
        ("东北亚", "东南亚", 38, -0.12),
        ("西欧", "非洲", 26, -0.12),
    ]

    fig = plt.figure(figsize=(16, 9), dpi=150)
    fig.patch.set_facecolor("#efefef")

    # 整页淡化世界地图水印
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    draw_world_map(bg, face="#d3d9e0", edge="#e2e7ec", lw=1.0, alpha=0.22, z=0)

    fig.text(
        0.03,
        0.94,
        "3.2.4 全球MEG物流：世界地图与区域平衡表",
        fontsize=27,
        fontweight="bold",
        color="#4a4a4a",
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2
        )
    )
    fig.lines.append(
        Line2D(
            [0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4
        )
    )
    fig.text(0.92, 0.945, "CIEC", fontsize=24, fontweight="bold", color="#5a5a5a")

    # 上半表格
    ax_table = fig.add_axes([0.03, 0.50, 0.94, 0.33])
    ax_table.set_axis_off()
    table = ax_table.table(
        cellText=table_rows,
        loc="center",
        cellLoc="center",
        colWidths=[
            0.08,
            0.08,
            0.08,
            0.07,
            0.08,
            0.08,
            0.08,
            0.07,
            0.08,
            0.12,
            0.08,
            0.07,
            0.08,
        ],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.35)

    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#4d4d4d")
        cell.set_linewidth(0.8)
        if r in (0, 1):
            cell.set_facecolor("#d9d9d9")
            cell.set_text_props(weight="bold", color="#2f2f2f")
        else:
            cell.set_facecolor("#f4f4f4")

    # 模拟“合并复合增速列单元格”
    for col, txt in zip((4, 8, 12), cagr_text):
        for r in range(2, 8):
            cell = table[r, col]
            cell.set_facecolor("#f7f7f7")
            if r == 2:
                cell.visible_edges = "TLR"
            elif r == 7:
                cell.visible_edges = "BLR"
            else:
                cell.visible_edges = "LR"
            cell.get_text().set_text("")
        center = table[4, col]
        center.get_text().set_text(txt)
        center.get_text().set_fontweight("bold")

    ax_table.text(
        0.75,
        1.05,
        "全球MEG物流（万吨）",
        ha="center",
        va="bottom",
        fontsize=14,
        color="#3d3d3d",
        fontweight="bold",
    )

    # 中间说明
    ax_note = fig.add_axes([0.04, 0.42, 0.92, 0.07])
    ax_note.set_axis_off()
    ax_note.text(
        0.0,
        0.55,
        "- 亚太缺口继续扩大，进口依赖上升；美洲小幅净进口；欧洲、中东及非洲净出口继续收窄。",
        fontsize=12.5,
        color="#3f3f3f",
    )
    ax_note.text(
        0.0,
        0.10,
        "- 2025年主干物流仍为中东/北美流向亚洲，欧洲补给来源维持中东+北美。",
        fontsize=12.5,
        color="#3f3f3f",
    )

    # 下半地图（按参考图样式：灰底+蓝色世界地图背景）
    ax_map = fig.add_axes([0.04, 0.08, 0.92, 0.33], facecolor="#ececec")
    ax_map.set_xlim(0, 1)
    ax_map.set_ylim(0, 1)
    ax_map.axis("off")
    draw_world_map(ax_map, face="#86a9c6", edge="#86a9c6", lw=0.6, alpha=1.0, z=1)

    ax_map.text(
        0.50,
        0.95,
        "2025年MEG全球物流标注（单位：万吨）",
        ha="center",
        va="center",
        fontsize=15,
        color="#303030",
    )
    ax_map.text(
        0.06,
        0.88,
        "Importer",
        fontsize=10,
        color="white",
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="round,pad=0.35,rounding_size=0.8",
            facecolor="#8c857f",
            edgecolor="none",
        ),
    )
    ax_map.text(
        0.15,
        0.88,
        "Exporter",
        fontsize=10,
        color="#4a3d1d",
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="round,pad=0.35,rounding_size=0.8",
            facecolor="#f4bf42",
            edgecolor="none",
        ),
    )

    add_trade_tag(
        ax_map,
        anchors["北美"][0],
        anchors["北美"][1],
        "N. America",
        165,
        85,
        dx=-0.00,
        dy=0.12,
    )
    add_trade_tag(
        ax_map,
        anchors["西欧"][0],
        anchors["西欧"][1],
        "W. Europe",
        95,
        26,
        dx=0.00,
        dy=0.12,
    )
    add_trade_tag(
        ax_map,
        anchors["中东"][0],
        anchors["中东"][1],
        "Middle East",
        70,
        320,
        dx=0.00,
        dy=0.12,
    )
    add_trade_tag(
        ax_map,
        anchors["东北亚"][0],
        anchors["东北亚"][1],
        "NE Asia",
        320,
        45,
        dx=0.00,
        dy=0.11,
    )
    add_trade_tag(
        ax_map,
        anchors["南亚"][0],
        anchors["南亚"][1],
        "South Asia",
        190,
        20,
        dx=-0.03,
        dy=0.10,
    )
    add_trade_tag(
        ax_map,
        anchors["东南亚"][0],
        anchors["东南亚"][1],
        "SE Asia",
        170,
        38,
        dx=0.10,
        dy=0.08,
    )
    add_trade_tag(
        ax_map,
        anchors["南美"][0],
        anchors["南美"][1],
        "S. America",
        55,
        10,
        dx=-0.02,
        dy=-0.08,
    )
    add_trade_tag(
        ax_map,
        anchors["非洲"][0],
        anchors["非洲"][1],
        "Africa",
        70,
        8,
        dx=0.02,
        dy=-0.10,
    )

    level_style = {
        1: {"color": "#f2a36b", "lw": 1.0, "ms": 6, "alpha": 0.78, "z": 2},
        2: {"color": "#e24a33", "lw": 2.2, "ms": 10, "alpha": 0.88, "z": 3},
        3: {"color": "#8b0000", "lw": 3.8, "ms": 14, "alpha": 0.96, "z": 4},
    }

    for src, dst, val, rad in flows:
        x1, y1 = anchors[src]
        x2, y2 = anchors[dst]
        if val >= 250:
            lvl = 3
        elif val >= 100:
            lvl = 2
        else:
            lvl = 1
        style = level_style[lvl]
        ax_map.add_patch(
            FancyArrowPatch(
                (x1, y1),
                (x2, y2),
                arrowstyle="-|>",
                mutation_scale=style["ms"],
                linewidth=style["lw"],
                color=style["color"],
                alpha=style["alpha"],
                connectionstyle=f"arc3,rad={rad}",
                zorder=style["z"],
            )
        )

    legend_handles = [
        Line2D([0], [0], color="#f2a36b", lw=1.0, label="1级流量（<100）"),
        Line2D([0], [0], color="#e24a33", lw=2.2, label="2级流量（100-250）"),
        Line2D([0], [0], color="#8b0000", lw=3.8, label="3级流量（>250）"),
    ]
    ax_map.legend(
        handles=legend_handles,
        loc="lower left",
        bbox_to_anchor=(0.01, -0.02),
        frameon=True,
        edgecolor="#9a9a9a",
        ncol=3,
        fontsize=9,
    )

    fig.text(
        0.98,
        0.012,
        "数据来源：TrendEconomy（HS290531）与公开行业资料整理（2020-2025，估算口径）；图表以定性分析为主",
        ha="right",
        fontsize=9,
        color="#666666",
    )

    fig.savefig(
        "results/pictures/meg-global-logistics.png", dpi=170, bbox_inches="tight"
    )
    fig.savefig("results/pictures/meg-global-logistics.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
