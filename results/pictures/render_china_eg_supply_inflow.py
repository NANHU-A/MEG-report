import os
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

    supply_gap = np.array([-12.4, -4.0, -10.2, -16.7, -14.7])
    net_inflow = np.array([830.2, 747.1, 704.5, 638.7, 757.3])

    fig = plt.figure(figsize=(16, 9), dpi=160)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_world_like_bg(bg)

    fig.text(0.03, 0.94, "4.3 中国平衡：", fontsize=28, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.5))
    fig.lines.append(Line2D([0.03, 0.115], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.0))
    fig.text(0.92, 0.945, "CIEC", fontsize=30, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.12, 0.26, 0.58, 0.34], facecolor="none")
    x = np.arange(len(years))

    ax.plot(x, supply_gap, color="#4f81bd", lw=2.4, label="供应缺口（-Δ库存）", zorder=3)
    ax.plot(x, net_inflow, color="#c0504d", lw=2.4, label="净流入量", zorder=3)
    ax.axhline(0, color="#b7b7b7", lw=0.9, alpha=0.8, zorder=1)

    for i, v in enumerate(supply_gap):
        ax.text(i, v - 18, f"{v:.1f}", ha="center", va="top", fontsize=10.5, color="#4f81bd")
    for i, v in enumerate(net_inflow):
        ax.text(i, v + 16, f"{v:.1f}", ha="center", va="bottom", fontsize=10.5, color="#c0504d")

    ax.set_xlim(-0.15, len(years) - 0.85)
    ax.set_ylim(-40, 900)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{y}" for y in years], fontsize=11, rotation=90)
    ax.set_yticks([0, 200, 400, 600, 800])
    ax.tick_params(axis="y", labelsize=12)
    ax.set_title("中国EG供应及流入（万吨）", fontsize=16, pad=15)
    
    ax.grid(axis="y", color="#d0d0d0", lw=1.1, alpha=0.7)

    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)
    ax.tick_params(axis="x", pad=10)

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False, fontsize=11)
    fig.text(0.50, 0.03, "数据来源：CCF等公开行业资料整理（2021-2025）；供应缺口= -Δ库存", ha="center", fontsize=13, color="#222")

    os.makedirs("results/pictures", exist_ok=True)
    out_png = "results/pictures/china_eg_supply_inflow.png"
    out_svg = "results/pictures/china_eg_supply_inflow.svg"
    fig.savefig(out_png, dpi=170, bbox_inches="tight")
    fig.savefig(out_svg, bbox_inches="tight")
    print(f"saved to {out_png} and {out_svg}")

if __name__ == "__main__":
    main()
