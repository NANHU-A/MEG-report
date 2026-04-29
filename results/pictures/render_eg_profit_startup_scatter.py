# -*- coding: utf-8 -*-
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def add_bg(ax):
    blobs = [
        (0.42, 0.55, 0.52, 0.26),
        (0.58, 0.50, 0.36, 0.22),
        (0.73, 0.44, 0.24, 0.15),
        (0.30, 0.46, 0.20, 0.13),
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
                alpha=0.22,
                zorder=0,
            )
        )


def main():
    os.makedirs("results/pictures", exist_ok=True)

    years = np.array([2021, 2022, 2023, 2024, 2025])

    # Estimated EG cash flow/profit
    cash_flow = np.array([120, -1200, -850, -450, -50], dtype=float)
    
    # Annual utilization-rate approximations based on EG context
    utilization_rate = np.array([68.0, 56.0, 58.0, 62.0, 63.0])
    
    # Estimated inventory days (port + plant)
    inventory_days = np.array([24.0, 38.0, 32.0, 26.0, 22.0])

    # Fit line for the scatter
    coef = np.polyfit(cash_flow, utilization_rate, 1)
    xfit = np.linspace(cash_flow.min() - 100, cash_flow.max() + 100, 200)
    yfit = np.polyval(coef, xfit)

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.94, "MEG：利润与产能利用率的背离（2021-2025）", fontsize=28, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.5))
    fig.lines.append(Line2D([0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.0))
    fig.text(0.50, 0.885, "成本结构差异与装置集中投产导致利润修复与开工率回升出现阶段性错位", ha="center", fontsize=12.4, color="#c81d24")
    fig.text(0.92, 0.945, "CIEC", fontsize=26, fontweight="bold", color="#5a5a5a")

    ax = fig.add_axes([0.08, 0.24, 0.76, 0.55], facecolor="none")
    ax2 = ax.twinx()

    # Main scatter
    ax.scatter(
        cash_flow,
        utilization_rate,
        s=165,
        color="#3d66ad",
        edgecolors="#1f2a3a",
        linewidth=1.1,
        zorder=4,
    )
    ax.plot(xfit, yfit, color="#ec7c2d", lw=2.8, linestyle="--", zorder=3)

    # Year labels
    offsets = {
        2021: (-8, 1.2, "center", "bottom"),
        2022: (4, -1.3, "center", "bottom"),
        2023: (4, 1.0, "center", "bottom"),
        2024: (-16, 3.0, "right", "bottom"),
        2025: (16, -4.0, "left", "top"),
    }
    for i, year in enumerate(years):
        dx, dy, ha, va = offsets[int(year)]
        ax.annotate(
            str(year),
            (cash_flow[i], utilization_rate[i]),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=11.0,
            fontweight="bold",
            color="#333333",
            ha=ha,
            va=va,
            zorder=6,
        )

    # Inventory on right axis
    ax2.plot(cash_flow, inventory_days, color="#7ea6bf", lw=2.1, linestyle="-.", marker="s", ms=6.0, alpha=0.95, zorder=2)
    for i, v in enumerate(inventory_days):
        ax2.text(cash_flow[i], v + 0.7, f"{v:.0f}", ha="center", va="bottom", fontsize=9.0, color="#5a7083")

    # Axes and style
    ax.set_xlabel("MEG行业模拟平均利润（元/吨）", fontsize=13, fontweight="bold", color="#333333")
    ax.set_ylabel("年均产能利用率（%）", fontsize=13, fontweight="bold", color="#3d66ad")
    ax2.set_ylabel("行业库存周转天数（天）", fontsize=13, fontweight="bold", color="#5a7083")
    
    ax.set_xlim(cash_flow.min() - 150, cash_flow.max() + 150)
    ax.set_ylim(50, 75)
    ax2.set_ylim(15, 45)
    ax.grid(True, linestyle=":", alpha=0.55, color="#9a9a9a")
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", length=0)
    ax2.tick_params(axis="y", length=0, colors="#5a7083")
    ax.tick_params(axis="y", colors="#3d66ad")
    for sp in ["top", "right", "left", "bottom"]:
        ax.spines[sp].set_visible(False)
        ax2.spines[sp].set_visible(False)

    # Legend
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor="#3d66ad", markeredgecolor="#1f2a3a", markersize=9, label="年均产能利用率散点"),
        Line2D([0], [0], color="#ec7c2d", lw=2.8, linestyle="--", label="利润拟合线"),
        Line2D([0], [0], color="#7ea6bf", lw=2.1, linestyle="-.", marker="s", markersize=6, label="库存天数（右轴）"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.47, -0.18), ncol=3, frameon=False, fontsize=10.6)

    # Notes
    fig.text(0.08, 0.12, "注：X为模拟平均利润，Y为年均产能利用率，右轴为行业港口及厂库周转天数估算；数据为拟合近似", fontsize=11.8, color="#222")
    fig.text(0.08, 0.085, "说明：背离受EO/EG价差排产切换、煤制季节性检修、以及阶梯式产能投放压制等行业特性影响", fontsize=11.6, color="#222")
    fig.text(
        0.08,
        0.035,
        "结论：MEG利润与开工总体正相关，但因装置联产及庞大基数，利润修复未完全传导至开工回升",
        fontsize=12.6,
        color="#111",
        bbox=dict(facecolor="white", alpha=0.88, edgecolor="#d0d0d0", boxstyle="round,pad=0.30"),
    )

    fig.savefig("results/pictures/eg_profit_startup_scatter.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/eg_profit_startup_scatter.svg", bbox_inches="tight")
    print("Charts successfully exported to results/pictures/")


if __name__ == "__main__":
    main()
