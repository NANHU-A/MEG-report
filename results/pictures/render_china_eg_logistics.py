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

def draw_simplified_china(ax, face="#dee4eb", edge="#f7f9fb", lw=1.1, alpha=1.0, z=1):
    # Simplified polygonal representation of China
    china_poly = [
        (0.75, 0.90), # NE
        (0.85, 0.85),
        (0.88, 0.70), # East
        (0.92, 0.50), # Shanghai/Zhejiang
        (0.85, 0.35), # Fujian
        (0.75, 0.20), # Guangdong
        (0.65, 0.15), # Guangxi/Hainan
        (0.50, 0.25), # Yunnan/Tibet
        (0.30, 0.35), # Tibet
        (0.10, 0.55), # Xinjiang
        (0.20, 0.75), # Xinjiang North
        (0.40, 0.70), # Gansu/Inner Mongolia
        (0.55, 0.85), # Inner Mongolia
        (0.65, 0.80), # Hebei
    ]
    ax.add_patch(
        Polygon(
            china_poly,
            closed=True,
            facecolor=face,
            edgecolor=edge,
            linewidth=lw,
            alpha=alpha,
            zorder=z,
        )
    )

def add_region_tag(ax, x, y, name, production, consumption, dx=0.0, dy=0.0):
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
        fontsize=9,
        color="white",
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.24,rounding_size=0.95",
            facecolor="#7f6f6d",
            edgecolor="none",
        ),
        zorder=6,
    )
    # Production
    ax.text(
        x0 + w1 + w2 / 2,
        y0,
        f"{production}",
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
    # Consumption
    ax.text(
        x0 + w1 + w2 + w3 / 2,
        y0,
        f"{consumption}",
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
    ax.scatter([x], [y], s=15, color="#555555", zorder=5)


def add_flow_label(ax, x, y, text):
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=8, color="#333333", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#cccccc", alpha=0.85),
        zorder=7
    )

def main():
    fig = plt.figure(figsize=(16, 9), dpi=150)
    fig.patch.set_facecolor("#efefef")

    # Background layer
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)

    fig.text(
        0.03,
        0.94,
        "3.2.5 中国EG物流流向（2025）",
        fontsize=27,
        fontweight="bold",
        color="#4a4a4a",
    )
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2))
    fig.lines.append(Line2D([0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4))
    fig.text(0.92, 0.945, "CIEC", fontsize=24, fontweight="bold", color="#5a5a5a")

    ax_note = fig.add_axes([0.04, 0.78, 0.92, 0.10])
    ax_note.set_axis_off()
    ax_note.text(0.0, 0.65, "核心驱动逻辑：", fontsize=14, fontweight="bold", color="#3f3f3f")
    ax_note.text(0.0, 0.35, "- 产能西移与北移：煤制EG主产区集中在西北（内蒙、陕西）与华北，形成规模化低成本供应。", fontsize=12.5, color="#3f3f3f")
    ax_note.text(0.0, 0.05, "- 消费高度集中：江浙及福建占据全国绝大部分聚酯产能，华东及华南为核心净流入区。", fontsize=12.5, color="#3f3f3f")

    ax_map = fig.add_axes([0.04, 0.08, 0.92, 0.68], facecolor="#ececec")
    ax_map.set_xlim(0, 1)
    ax_map.set_ylim(0, 1)
    ax_map.axis("off")
    
    draw_simplified_china(ax_map, face="#d3d9e0", edge="#ffffff", lw=2.0, alpha=0.6, z=1)

    ax_map.text(0.50, 0.95, "2025年国内MEG主干物流及供需流向估算（单位：万吨/年）", ha="center", va="center", fontsize=15, color="#303030", fontweight="bold")
    
    ax_map.text(0.06, 0.88, "产量", fontsize=10, color="white", fontweight="bold", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.8", facecolor="#8c857f", edgecolor="none"))
    ax_map.text(0.12, 0.88, "消费量", fontsize=10, color="#4a3d1d", fontweight="bold", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.8", facecolor="#f4bf42", edgecolor="none"))

    anchors = {
        "西北 (陕蒙为主)": (0.45, 0.65),
        "华北": (0.65, 0.60),
        "东北": (0.80, 0.80),
        "华东 (江浙为主)": (0.82, 0.45),
        "华南 (含福建)": (0.70, 0.25),
        "海外进口": (0.92, 0.15)
    }

    add_region_tag(ax_map, anchors["西北 (陕蒙为主)"][0], anchors["西北 (陕蒙为主)"][1], "西北", "1,050", 10, dx=-0.0, dy=0.08)
    add_region_tag(ax_map, anchors["华北"][0], anchors["华北"][1], "华北", 280, 50, dx=0.0, dy=0.08)
    add_region_tag(ax_map, anchors["东北"][0], anchors["东北"][1], "东北", 150, 10, dx=0.0, dy=0.08)
    add_region_tag(ax_map, anchors["华东 (江浙为主)"][0], anchors["华东 (江浙为主)"][1], "华东", "1,200", "1,800", dx=0.08, dy=0.0)
    add_region_tag(ax_map, anchors["华南 (含福建)"][0], anchors["华南 (含福建)"][1], "华南", 550, 600, dx=0.0, dy=-0.08)
    add_region_tag(ax_map, anchors["海外进口"][0], anchors["海外进口"][1], "海外进口", "-", "-", dx=0.0, dy=-0.05)

    flows = [
        ("西北 (陕蒙为主)", "华东 (江浙为主)", "600", 0.1, 3),
        ("西北 (陕蒙为主)", "华南 (含福建)", "300", 0.2, 2),
        ("华北", "华东 (江浙为主)", "200", 0.1, 2),
        ("华北", "华南 (含福建)", "50", -0.1, 1),
        ("东北", "华东 (江浙为主)", "100", -0.2, 2),
        ("东北", "华南 (含福建)", "40", -0.3, 1),
        ("海外进口", "华东 (江浙为主)", "300", 0.1, 3),
        ("海外进口", "华南 (含福建)", "250", -0.1, 2),
    ]

    level_style = {
        1: {"color": "#f2a36b", "lw": 1.5, "ms": 8, "alpha": 0.85, "z": 2},
        2: {"color": "#e24a33", "lw": 3.0, "ms": 12, "alpha": 0.90, "z": 3},
        3: {"color": "#8b0000", "lw": 4.5, "ms": 16, "alpha": 0.95, "z": 4},
    }

    for src, dst, val, rad, lvl in flows:
        x1, y1 = anchors[src]
        x2, y2 = anchors[dst]
        style = level_style[lvl]
        ax_map.add_patch(
            FancyArrowPatch(
                (x1, y1), (x2, y2),
                arrowstyle="-|>",
                mutation_scale=style["ms"],
                linewidth=style["lw"],
                color=style["color"],
                alpha=style["alpha"],
                connectionstyle=f"arc3,rad={rad}",
                zorder=style["z"],
            )
        )
        
        # Add a text label near the midpoint of the connection
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        if rad > 0:
            mx -= rad * (y2 - y1) * 0.3
            my += rad * (x2 - x1) * 0.3
        else:
            mx -= rad * (y2 - y1) * 0.3
            my += rad * (x2 - x1) * 0.3
            
        add_flow_label(ax_map, mx, my, val)

    legend_handles = [
        Line2D([0], [0], color="#f2a36b", lw=1.5, label="辅助流量（<100万吨）"),
        Line2D([0], [0], color="#e24a33", lw=3.0, label="主要干线（100-300万吨）"),
        Line2D([0], [0], color="#8b0000", lw=4.5, label="核心干线（>300万吨）"),
    ]
    ax_map.legend(
        handles=legend_handles,
        loc="lower left",
        bbox_to_anchor=(0.01, 0.02),
        frameon=True,
        edgecolor="#9a9a9a",
        ncol=1,
        fontsize=10,
    )

    fig.text(
        0.98,
        0.02,
        "数据来源：公开行业资料及投产计划整理（2025估算口径）；本图以定性分析流向及大致量级为主",
        ha="right",
        fontsize=9,
        color="#666666",
    )

    fig.savefig("results/pictures/china-eg-logistics-2025.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/china-eg-logistics-2025.svg", bbox_inches="tight")
    print("saved results/pictures/china-eg-logistics-2025.png")

if __name__ == "__main__":
    main()