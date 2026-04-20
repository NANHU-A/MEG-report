import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def draw_card(ax, x, y, w, h, title, lines, fc, ec, badge):
    card = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.02",
        facecolor=fc,
        edgecolor=ec,
        linewidth=1.8,
        zorder=2,
    )
    ax.add_patch(card)

    ax.text(x + 0.015, y + h - 0.035, title, fontsize=14.5, fontweight="bold", color="#22303a", zorder=3)

    by = y + h - 0.070
    for t in lines:
        ax.text(x + 0.018, by, t, fontsize=11.2, color="#1f2a33", zorder=3)
        by -= 0.030

    badge_box = FancyBboxPatch(
        (x + w - 0.125, y + h - 0.045),
        0.11,
        0.028,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor="#ffffff",
        edgecolor=ec,
        linewidth=1.2,
        zorder=4,
    )
    ax.add_patch(badge_box)
    ax.text(x + w - 0.070, y + h - 0.031, badge, fontsize=9.8, color="#2d3a45", ha="center", va="center", zorder=5)


def main():
    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#f2f3f5")

    fig.text(0.03, 0.94, "全球EG供应端边际成本梯队图", fontsize=30, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
    fig.lines.append(Line2D([0.03, 0.14], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.2))
    fig.text(0.92, 0.945, "CIEC", fontsize=27, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.03, 0.08, 0.94, 0.80])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 成本递增主箭头（左 -> 右）
    ax.add_patch(
        FancyArrowPatch(
            (0.03, 0.95),
            (0.98, 0.95),
            arrowstyle="-|>",
            mutation_scale=20,
            linewidth=2.2,
            color="#6e6e6e",
            alpha=0.9,
        )
    )
    ax.text(0.03, 0.965, "低成本", fontsize=12.5, color="#3f3f3f", va="bottom")
    ax.text(0.98, 0.965, "高成本", fontsize=12.5, color="#3f3f3f", va="bottom", ha="right")

    # 六个梯队卡片
    cards = [
        (
            0.02,
            0.58,
            0.30,
            0.30,
            "第一梯队｜一体化油制EG（最低成本）",
            [
                "工艺：原油/石脑油/LPG → 裂解乙烯 → EO → EG",
                "成本特征：炼化+园区一体化，自有乙烯，协同效率最高",
                "地区：中东（沙特/阿联酋/卡塔尔/科威特）",
                "      北美部分一体化装置、新加坡大型园区",
                "供给属性：全球低成本基荷产能，最先开工、最先恢复",
            ],
            "#e9f6ea",
            "#5aa35a",
            "低成本基荷",
        ),
        (
            0.35,
            0.58,
            0.30,
            0.30,
            "第二梯队｜大型石化园区油制EG（中低成本）",
            [
                "工艺：石脑油/乙烯 → EO → EG",
                "成本特征：一体化程度较好，但弱于第一梯队",
                "地区：韩国 / 中国台湾 / 日本 / 中国沿海大型园区",
                "典型原料：石脑油、园区配套乙烯",
                "供给属性：稳定供给，利润中枢偏稳",
            ],
            "#eef6ff",
            "#5a8bc5",
            "稳定供给",
        ),
        (
            0.68,
            0.58,
            0.30,
            0.30,
            "第三梯队｜外采乙烯油制EG（中成本）",
            [
                "工艺：外采乙烯 → EO → EG",
                "成本特征：对乙烯价格敏感，利润弹性大",
                "地区：中国 / 东南亚 / 印度部分地区 / 欧洲部分装置",
                "典型原料：外购乙烯",
                "供给属性：典型边际供给，波动期最先降负",
            ],
            "#f0f5ff",
            "#4f74ad",
            "边际供给",
        ),
        (
            0.10,
            0.18,
            0.26,
            0.30,
            "第四梯队｜高效率煤制EG（中高成本）",
            [
                "工艺：煤/天然气 → 合成气 → DMO(草酸酯法) → EG",
                "成本特征：受煤价、电价、公用工程影响大",
                "地区：中国（全球最主要煤制产能）",
                "供给属性：国内重要边际供给，利润驱动开工明显",
            ],
            "#fff6e8",
            "#df9b3f",
            "边际供给",
        ),
        (
            0.40,
            0.18,
            0.26,
            0.30,
            "第五梯队｜一般煤制/高成本边际装置（高成本）",
            [
                "工艺：煤制EG",
                "成本特征：效率低、能耗高、折旧重、环保约束强",
                "地区：中国部分老旧或低效率装置",
                "供给属性：高价才维持，低价最先减产/停车",
            ],
            "#fff2e9",
            "#d97543",
            "高成本出清",
        ),
        (
            0.70,
            0.18,
            0.26,
            0.30,
            "第六梯队｜老旧/小规模/物流受限装置（最高成本）",
            [
                "工艺：油制或煤制均可能",
                "成本特征：原料采购不灵活、公用工程弱、运输受限",
                "地区：区域性小装置、部分新兴市场",
                "供给属性：极端行情下最后供给（出清产能）",
            ],
            "#ffecea",
            "#ca5a50",
            "高成本出清",
        ),
    ]

    for c in cards:
        draw_card(ax, *c)

    # 右上角动态说明框
    note = FancyBboxPatch(
        (0.70, 0.90),
        0.27,
        0.08,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        facecolor="#ffffff",
        edgecolor="#8d8d8d",
        linewidth=1.2,
        zorder=6,
    )
    ax.add_patch(note)
    ax.text(0.715, 0.947, "动态提示：边际成本会随乙烯、煤、电价格变化而移动", fontsize=11.3, color="#30363d", zorder=7)

    # 图例
    legend_x, legend_y = 0.02, 0.02
    ax.text(legend_x, legend_y + 0.07, "图例", fontsize=12.5, fontweight="bold", color="#2f3b46")
    legend_items = [
        ("#4f74ad", "油制"),
        ("#d97543", "煤制"),
        ("#5aa35a", "一体化"),
        ("#7f7f7f", "外采原料"),
    ]
    lx = legend_x
    for color, text in legend_items:
        ax.add_patch(Rectangle((lx, legend_y + 0.02), 0.018, 0.018, facecolor=color, edgecolor="none", zorder=6))
        ax.text(lx + 0.022, legend_y + 0.029, text, fontsize=10.5, va="center", color="#2f3b46")
        lx += 0.12

    # 研究结论（必须体现）
    fig.text(0.03, 0.035, "结论：低成本供给主要来自中东+一体化油制；中国煤制是重要但偏高成本边际供给；外采乙烯油制与低效率煤制在下跌周期更易减产。", fontsize=12.5, color="#2c2c2c")
    fig.text(0.50, 0.012, "注：边际成本为动态概念，受乙烯、煤价、电价、装置效率及一体化程度影响，图中排序为研究框架下的近似梯队。", ha="center", fontsize=11.5, color="#4f4f4f")

    fig.savefig("results/pictures/eg-marginal-cost-ladder.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg-marginal-cost-ladder.svg", bbox_inches="tight")
    print("saved")


if __name__ == "__main__":
    main()
