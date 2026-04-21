import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def factor(status: str) -> float:
    s = status.replace(" ", "")
    if "运行中，负荷下降" in s or "降负荷运行中" in s or "降负至50%以下" in s:
        return 0.70
    if "运行中" in s and "负荷下降" not in s:
        return 1.00
    if "近日重启" in s or "近日已起" in s or "重启中" in s:
        return 0.50
    if "检修" in s or "开停车" in s or "开车" in s or "待定" in s or "无明确计划" in s or "目前未起启" in s:
        return 0.30
    if "停车" in s or "停产" in s:
        return 0.00
    return 0.50


def parse_capacity(text: str) -> float:
    return sum(float(x) for x in text.split("+") if x)


def region_of(location: str) -> str:
    if location in ["中国台湾", "日本", "韩国", "新加坡", "泰国", "马来西亚", "印度"]:
        return "亚洲"
    if location in ["沙特", "科威特", "伊朗"]:
        return "中东"
    if location in ["加拿大", "美国"]:
        return "北美"
    return "其他"


records = [
    ("南亚1#", "36", "中国台湾", "停车中"),
    ("南亚2#", "36", "中国台湾", "停车中"),
    ("南亚3#", "36", "中国台湾", "4.1开始停车，重启时间待定"),
    ("南亚4#", "72", "中国台湾", "停车中"),
    ("台湾中纤", "20", "中国台湾", "2月上旬开始停车，目前未起启"),
    ("台湾东联", "25", "中国台湾", "降负荷运行中"),
    ("熊猫", "10.5", "日本", "运行中"),
    ("李沙汽达尔", "12", "韩国", "降负至50%以下"),
    ("乐天丽水A", "12+12", "韩国", "3月上旬开始执行检修，预计持续至5月底"),
    ("乐天丽水B", "16", "韩国", "停车中，重启待定"),
    ("KPIC", "18.5", "韩国", "停车中"),
    ("kayan", "85", "沙特", "停车中"),
    ("yansab", "91", "沙特", "运行中"),
    ("sharq1", "45", "沙特", "停车中"),
    ("Sharq2", "45", "沙特", "停车中"),
    ("Sharq3", "55", "沙特", "近日已起启"),
    ("Sharq4", "70", "沙特", "近日重启中"),
    ("yanpet1", "38", "沙特", "停车中"),
    ("yanpet2", "52", "沙特", "运行中"),
    ("JUPC1", "70", "沙特", "停车中"),
    ("JUPC2", "64", "沙特", "停车中"),
    ("JUPC3", "70", "沙特", "停车中"),
    ("Equate1#", "53", "科威特", "运行中，负荷下降"),
    ("Equate2#", "61.5", "科威特", "3月上旬开始停车，重启时间未确定"),
    ("Meglobal1", "46", "加拿大", "运行中"),
    ("Meglobal2", "44", "加拿大", "运行中"),
    ("Meglobal3", "45", "加拿大", "运行中"),
    ("Farsa", "40", "伊朗", "停车中"),
    ("Monerid", "50", "伊朗", "停车中"),
    ("Marun", "44.5", "伊朗", "停车中"),
    ("拉比格炼化", "70", "沙特", "运行中"),
    ("三井", "11.5", "日本", "运行中"),
    ("Aster", "90", "新加坡", "停车中"),
    ("泰国PTT", "40", "泰国", "运行中"),
    ("乐天", "70", "美国", "运行中"),
    ("马来西亚石油A", "38", "马来西亚", "3月下旬开始停车检修，预计持续至5月底"),
    ("马来西亚石油B", "75", "马来西亚", "停车中"),
    ("南亚（新）", "82.8", "美国", "运行中"),
    ("南亚", "36", "美国", "3月下旬初始停车"),
    ("Sasol", "28", "美国", "运行中"),
    ("壳牌A", "12.5", "美国", "运行中"),
    ("壳牌B", "25", "美国", "运行中"),
    ("Shell", "50", "加拿大", "运行中"),
    ("MEGlobal", "103", "美国", "运行中"),
    ("Indorama", "34", "美国", "运行中，检修推后"),
    ("GCGV", "110", "美国", "运行中"),
    ("IOC", "40", "印度", "运行中"),
    ("BCCO", "45", "伊朗", "停车中"),
    ("SPII", "50", "伊朗", "计划3月上旬开车，目前无明确计划"),
]

for r in records:
    pass

data = []
for name, cap_text, loc, status in records:
    cap = parse_capacity(cap_text)
    reg = region_of(loc)
    fac = factor(status)
    data.append((name, cap, loc, status, reg, fac, cap * fac))

regions = ["中东", "亚洲", "北美"]
region_colors = {"中东": "#d84a3a", "亚洲": "#edc948", "北美": "#59a14f"}

summary = {}
for reg in regions:
    items = [d for d in data if d[4] == reg]
    nominal = sum(d[1] for d in items)
    effective = sum(d[6] for d in items)
    summary[reg] = {"nominal": nominal, "effective": effective, "util": effective / nominal if nominal else 0}

fig = plt.figure(figsize=(16, 9), dpi=170)
fig.patch.set_facecolor("#f3f5f7")

fig.text(0.03, 0.94, "EG全球装置运行状态：地区整合后的有效产能", fontsize=28, fontweight="bold", color="#4a4a4a")
fig.lines.append(Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2.4))
fig.lines.append(Line2D([0.03, 0.14], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4.1))

ax = fig.add_axes([0.08, 0.18, 0.68, 0.60])
ax.set_facecolor("#ffffff")

x = np.arange(len(regions))
nominal = np.array([summary[r]["nominal"] for r in regions])
effective = np.array([summary[r]["effective"] for r in regions])

ax.bar(x, nominal, width=0.52, color="#d9dde3", edgecolor="#87919b", linewidth=1.2, label="名义产能")
ax.bar(x, effective, width=0.52, color=[region_colors[r] for r in regions], edgecolor="none", label="有效产能")

for i, r in enumerate(regions):
    ax.text(i, nominal[i] + 18, f"{nominal[i]:.1f}", ha="center", va="bottom", fontsize=11, color="#666")
    ax.text(i, effective[i] + 18, f"{effective[i]:.1f}", ha="center", va="bottom", fontsize=12, fontweight="bold", color="#111")
    ax.text(i, -65, f"{r}\n利用率 {summary[r]['util']*100:.0f}%", ha="center", va="top", fontsize=12, color="#2f3b46")

ax.set_xticks(x)
ax.set_xticklabels(["中东", "亚洲", "北美"], fontsize=13)
ax.set_ylabel("万吨", fontsize=13)
ax.set_ylim(0, max(nominal) * 1.20)
ax.grid(axis="y", color="#d6dbe0", lw=0.9)
ax.set_axisbelow(True)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

ax.legend(loc="upper left", frameon=False, fontsize=11)

note = FancyBboxPatch((0.80, 0.67), 0.17, 0.19, boxstyle="round,pad=0.012,rounding_size=0.018", facecolor="#fff", edgecolor="#8d8d8d", linewidth=1.1, transform=fig.transFigure)
fig.patches.append(note)
fig.text(0.815, 0.82, "2025年Q2三分化\n中东大量停车\n亚洲春季检修\n北美稳定运行", fontsize=14, color="#c00000")

fig.text(0.80, 0.60, "有效产能口径：\n运行=100%\n降负=70%\n检修/开停车=30%\n停车=0%", fontsize=11.5, color="#30363d")

fig.text(0.08, 0.08, "结论：供给端显著收缩，对EG价格形成有力支撑。", fontsize=14, color="#1f2a33")
fig.text(0.08, 0.05, "注：有效产能为根据表内装置状态做的近似加权整合，适合用于地区供给格局展示。", fontsize=11.5, color="#555")

fig.savefig("results/pictures/eg-q2-effective-capacity-by-region.png", dpi=170, bbox_inches="tight")
fig.savefig("results/pictures/eg-q2-effective-capacity-by-region.svg", bbox_inches="tight")
print("saved")
