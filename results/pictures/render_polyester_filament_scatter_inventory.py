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

    # User-provided cash flow table
    cf_poy = np.array([371, -126, 67, 135, 217], dtype=float)
    cf_fdy = np.array([29, -111, 246, 224, 45], dtype=float)
    cf_dty = np.array([404, 179, 189, 220, 56], dtype=float)
    w_poy, w_fdy, w_dty = 63.5, 29.8, 0.7
    cash_flow = (cf_poy * w_poy + cf_fdy * w_fdy + cf_dty * w_dty) / (w_poy + w_fdy + w_dty)
    cash_flow = np.round(cash_flow, 2)

    # Annual utilization-rate approximations based on the provided chart
    utilization_rate = np.array([79.0, 67.0, 78.0, 85.0, 85.0])
    inventory_days = np.array([15.0, 31.0, 24.0, 26.0, 28.0])

    # Fit line for the scatter
    coef = np.polyfit(cash_flow, utilization_rate, 1)
    xfit = np.linspace(cash_flow.min() - 20, cash_flow.max() + 20, 200)
    yfit = np.polyval(coef, xfit)

    fig = plt.figure(figsize=(16, 9), dpi=170)
    fig.patch.set_facecolor("#efefef")

    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    add_bg(bg)

    fig.text(0.03, 0.94, "涤纶长丝：现金流与产能利用率的背离（2021-2025）", fontsize=28, fontweight="bold", color="#4a4a4a")
    fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.5))
    fig.lines.append(Line2D([0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.0))
    fig.text(0.50, 0.885, "高库存阶段利润并非决定产能利用率的唯一因素，企业可能主动降负以稳价稳利", ha="center", fontsize=12.4, color="#c81d24")
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

    # Visible divergence callouts (no arrows)
    ax.text(
        cash_flow[1] - 58,
        utilization_rate[1] + 4.0,
        "背离点：\n利润转负，\n利用率仅小幅回落",
        fontsize=9.7,
        color="#8b0000",
        ha="left",
        va="center",
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#fff7f4", edgecolor="#e0b6a8"),
        zorder=7,
    )
    ax.text(
        cash_flow[4] + 12,
        utilization_rate[4] + 1.8,
        "背离点：\n现金流改善，\n利用率未继续抬升",
        fontsize=9.7,
        color="#8b0000",
        ha="left",
        va="center",
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#fff7f4", edgecolor="#e0b6a8"),
        zorder=7,
    )

    # Inventory on right axis
    ax2.plot(cash_flow, inventory_days, color="#7ea6bf", lw=2.1, linestyle="-.", marker="s", ms=6.0, alpha=0.95, zorder=2)
    for i, v in enumerate(inventory_days):
        ax2.text(cash_flow[i], v + 0.7, f"{v:.0f}", ha="center", va="bottom", fontsize=9.0, color="#5a7083")

    # Axes and style
    ax.set_xlabel("长丝加权年均现金流（元/吨）", fontsize=13, fontweight="bold", color="#333333")
    ax.set_ylabel("年均产能利用率（%）", fontsize=13, fontweight="bold", color="#3d66ad")
    ax2.set_ylabel("库存（天）", fontsize=13, fontweight="bold", color="#5a7083")
    ax.set_xlim(cash_flow.min() - 55, cash_flow.max() + 55)
    ax.set_ylim(64, 90)
    ax2.set_ylim(10, 35)
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
        Line2D([0], [0], color="#ec7c2d", lw=2.8, linestyle="--", label="现金流拟合线"),
        Line2D([0], [0], color="#7ea6bf", lw=2.1, linestyle="-.", marker="s", markersize=6, label="库存（右轴）"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.47, -0.18), ncol=3, frameon=False, fontsize=10.6)

    # Notes
    fig.text(0.08, 0.12, "注：X轴=长丝加权年均现金流，Y轴=年均产能利用率，右轴=行业库存；权重=POY:FDY:DTY=63.5:29.8:0.7。", fontsize=11.8, color="#222")
    fig.text(0.08, 0.085, "说明：产能利用率/库存为基于截图与公开行业文本的年度近似值。", fontsize=11.6, color="#222")
    fig.text(
        0.08,
        0.035,
        "结论：利润与开工率总体正相关，但库存会造成明显背离。",
        fontsize=12.6,
        color="#111",
        bbox=dict(facecolor="white", alpha=0.88, edgecolor="#d0d0d0", boxstyle="round,pad=0.30"),
    )

    fig.savefig("results/pictures/polyester_filament_scatter_inventory.png", dpi=170, bbox_inches="tight")
    fig.savefig("results/pictures/polyester_filament_scatter_inventory.svg", bbox_inches="tight")
    print("Charts successfully exported to results/pictures/")


if __name__ == "__main__":
    main()
