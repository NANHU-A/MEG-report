import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def add_world_like_bg(ax):
    blobs = [
        (0.45, 0.58, 0.55, 0.25),
        (0.57, 0.52, 0.35, 0.20),
        (0.36, 0.50, 0.25, 0.16),
        (0.70, 0.48, 0.22, 0.13),
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
                alpha=0.25,
                zorder=0,
            )
        )


plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False

fig = plt.figure(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor("#efefef")

bg = fig.add_axes([0, 0, 1, 1])
bg.set_axis_off()
add_world_like_bg(bg)

fig.text(
    0.03,
    0.94,
    "3.2.1 全球需求：全球消费结构（MEG）",
    fontsize=28,
    fontweight="bold",
    color="#4a4a4a",
)
bg.plot([0.03, 0.98], [0.90, 0.90], color="#4a4a4a", lw=2, transform=fig.transFigure)
bg.plot([0.03, 0.12], [0.90, 0.90], color="#c81d24", lw=4, transform=fig.transFigure)
fig.text(0.92, 0.945, "CIEC", fontsize=24, fontweight="bold", color="#5a5a5a")

ax1 = fig.add_axes([0.12, 0.30, 0.35, 0.45], facecolor="none")
ax2 = fig.add_axes([0.50, 0.30, 0.35, 0.45], facecolor="none")

labels1 = ["涤纶长丝", "聚酯瓶片", "涤纶短纤", "聚酯切片/薄膜", "防冻液", "溶剂/中间体"]
sizes1 = [50, 20, 11, 9, 5, 5]
colors1 = ["#3f67ad", "#ed7d31", "#70ad47", "#8064a2", "#ffc000", "#5b9bd5"]

res1 = ax1.pie(
    sizes1,
    labels=[f"{l}, {s}%" for l, s in zip(labels1, sizes1)],
    colors=colors1,
    startangle=90,
    counterclock=False,
    labeldistance=1.05,
    wedgeprops={"linewidth": 1.5, "edgecolor": "white"},
    textprops={"fontsize": 11},
)
wedges1, texts1 = res1[0], res1[1]
ax1.set_title("全球MEG下游消费结构", fontsize=18, pad=16)
ax1.set_aspect("equal")

labels2 = [
    "中国",
    "印度",
    "美国",
    "欧盟",
    "东南亚",
    "中东",
    "日本",
    "韩国",
    "土耳其",
    "其他国家",
]
sizes2 = [41.0, 10.5, 8.5, 7.5, 8.0, 6.0, 3.0, 2.5, 2.0, 11.0]
colors2 = [
    "#ed7d31",
    "#5b9bd5",
    "#4472c4",
    "#70ad47",
    "#00b0f0",
    "#ffc000",
    "#c55a11",
    "#7f7f7f",
    "#bf9000",
    "#8064a2",
]

res2 = ax2.pie(
    sizes2,
    labels=[f"{s:.1f}%" for s in sizes2],
    colors=colors2,
    startangle=90,
    counterclock=False,
    labeldistance=0.78,
    wedgeprops={"linewidth": 1.5, "edgecolor": "white"},
    textprops={"fontsize": 10},
)
wedges2, texts2 = res2[0], res2[1]
ax2.set_title("全球MEG下游消费国家", fontsize=18, pad=16)
ax2.set_aspect("equal")
ax2.legend(
    wedges2,
    labels2,
    loc="center left",
    bbox_to_anchor=(1.08, 0.5),
    fontsize=11,
    frameon=False,
    handlelength=0.8,
    handletextpad=0.4,
)

fig.text(
    0.12,
    0.16,
    "- MEG消费以聚酯链为核心（约90%），其中涤纶长丝与瓶片为主；非聚酯端（防冻液、溶剂/中间体）占比约10%。",
    fontsize=20,
)
fig.text(
    0.12,
    0.08,
    "- 中国为全球MEG消费第一大市场，印度与东南亚增速较快，消费结构与纺织、包装及出口产业链高度相关。",
    fontsize=20,
)

fig.savefig(
    "results/figures/meg-global-consumption-structure.png", dpi=150, bbox_inches="tight"
)
fig.savefig("results/figures/meg-global-consumption-structure.svg", bbox_inches="tight")
print("saved")
