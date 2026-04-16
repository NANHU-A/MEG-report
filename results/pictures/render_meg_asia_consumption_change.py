import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def add_world_bg(ax):
    shapes = [
        (0.50, 0.52, 0.60, 0.28),
        (0.62, 0.48, 0.34, 0.19),
        (0.39, 0.50, 0.26, 0.15),
        (0.73, 0.45, 0.20, 0.12),
    ]
    for x, y, w, h in shapes:
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


years = list(range(2009, 2026))
data = {
    "斯里兰卡": [
        8.5,
        10.7,
        11.2,
        11.0,
        10.7,
        8.6,
        12.7,
        14.2,
        12.8,
        13.4,
        11.3,
        11.1,
        10.7,
        11.4,
        8.2,
        8.4,
        8.7,
    ],
    "印尼": [
        42.6,
        43.8,
        47.4,
        54.8,
        58.0,
        58.7,
        54.1,
        60.8,
        63.0,
        65.3,
        64.0,
        59.8,
        61.4,
        62.8,
        60.3,
        61.1,
        62.0,
    ],
    "越南": [
        39.9,
        14.0,
        14.5,
        15.0,
        15.4,
        15.7,
        17.6,
        19.4,
        21.4,
        22.5,
        23.0,
        24.0,
        37.5,
        44.3,
        48.0,
        49.1,
        50.4,
    ],
    "马来西亚": [
        47.0,
        47.8,
        42.1,
        45.9,
        44.7,
        45.9,
        48.4,
        50.4,
        51.8,
        54.1,
        54.5,
        54.2,
        55.2,
        51.3,
        42.5,
        43.8,
        45.2,
    ],
    "菲律宾": [
        7.2,
        6.3,
        6.4,
        7.2,
        4.5,
        4.9,
        3.0,
        3.2,
        3.5,
        4.0,
        3.6,
        3.8,
        3.7,
        3.4,
        2.7,
        2.8,
        2.9,
    ],
    "泰国": [
        39.9,
        45.9,
        48.7,
        50.5,
        52.1,
        54.1,
        60.1,
        65.0,
        70.0,
        76.0,
        77.4,
        69.2,
        66.0,
        122.2,
        83.7,
        86.0,
        88.5,
    ],
    "中国": [
        304.0,
        342.0,
        360.2,
        389.0,
        427.0,
        480.4,
        468.0,
        489.6,
        538.6,
        567.0,
        567.4,
        555.5,
        594.9,
        580.5,
        654.1,
        669.0,
        684.0,
    ],
    "印度": [
        90.5,
        94.5,
        95.8,
        98.8,
        96.2,
        101.5,
        99.4,
        103.3,
        108.2,
        122.0,
        114.4,
        103.6,
        111.4,
        128.5,
        104.1,
        107.0,
        110.0,
    ],
}

df = pd.DataFrame(data, index=years)

fig = plt.figure(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor("#efefef")

bg = fig.add_axes([0, 0, 1, 1])
bg.set_axis_off()
add_world_bg(bg)

fig.text(
    0.03,
    0.94,
    "3.2.3 全球需求：亚洲消费量变化",
    fontsize=28,
    fontweight="bold",
    color="#4a4a4a",
)
fig.lines.append(
    plt.Line2D(
        [0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2
    )
)
fig.lines.append(
    plt.Line2D(
        [0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4
    )
)
fig.text(0.92, 0.945, "CIEC", fontsize=24, fontweight="bold", color="#5a5a5a")

# top table
ax_table = fig.add_axes([0.15, 0.50, 0.70, 0.34])
ax_table.set_axis_off()

table_df = df.T.copy()
table_df["复合增速"] = ((table_df[2025] / table_df[2009]) ** (1 / 16) - 1) * 100
display_cols = [2009, 2013, 2018, 2025, "复合增速"]
tbl = table_df[display_cols].copy()
tbl["复合增速"] = tbl["复合增速"].map(lambda x: f"{x:.1f}%")
for c in [2009, 2013, 2018, 2025]:
    tbl[c] = tbl[c].map(lambda x: f"{x:.1f}")

cell_text = tbl.values.tolist()
row_labels = tbl.index.tolist()
col_labels = ["2009", "2013", "2018", "2025", "复合增速"]

table = ax_table.table(
    cellText=cell_text,
    rowLabels=row_labels,
    colLabels=col_labels,
    loc="center",
    cellLoc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.3)
ax_table.text(
    0.5,
    1.04,
    "亚洲主要消费国（万吨）",
    ha="center",
    va="bottom",
    fontsize=14,
    transform=ax_table.transAxes,
)

# bottom stacked bars
ax = fig.add_axes([0.12, 0.10, 0.76, 0.33], facecolor="none")
ax.set_title("亚洲主要消费国实际消费量（万吨）", fontsize=18, pad=8)

colors = {
    "斯里兰卡": "#548235",
    "印尼": "#7f7f7f",
    "越南": "#ffc000",
    "马来西亚": "#a5a5a5",
    "菲律宾": "#70ad47",
    "泰国": "#5b9bd5",
    "中国": "#ed7d31",
    "印度": "#4472c4",
}

bottom = np.zeros(len(df.index))
for k in ["斯里兰卡", "印尼", "越南", "马来西亚", "菲律宾", "泰国", "中国", "印度"]:
    vals = df[k].values
    ax.bar(
        df.index,
        vals,
        bottom=bottom,
        width=0.42,
        color=colors[k],
        edgecolor="none",
        label=k,
        zorder=2,
    )
    bottom += vals

ax.set_xlim(2008.5, 2025.5)
ax.set_ylim(0, 1000)
ax.set_xticks(df.index)
ax.set_xticklabels(df.index, rotation=90)
ax.grid(axis="y", color="#cccccc", lw=0.8, alpha=0.8)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#bdbdbd")
ax.tick_params(axis="both", length=0)

ax.legend(
    ncol=8,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.10),
    frameon=False,
    fontsize=10,
    handlelength=0.8,
    columnspacing=0.8,
    handletextpad=0.3,
)

fig.text(
    0.5,
    0.008,
    "数据来源：wind数据库及公开资料整理（2009-2025）",
    ha="center",
    fontsize=16,
)

fig.savefig(
    "results/pictures/meg-asia-consumption-change.png", dpi=150, bbox_inches="tight"
)
fig.savefig("results/pictures/meg-asia-consumption-change.svg", bbox_inches="tight")
print("saved")
