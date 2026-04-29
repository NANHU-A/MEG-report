# Global MEG Logistics Figure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a template-consistent global MEG logistics figure (table + world map flow arrows) and export SVG/PNG to `results/pictures`.

**Architecture:** Use one Python matplotlib renderer script with embedded regional data tables and flow edges. Render in the same visual grammar as existing figures (gray background, title lines, CIEC tag, bottom source note), then export two formats from a single run.

**Tech Stack:** Python 3, matplotlib, numpy (optional), existing local font stack (Microsoft YaHei/SimHei).

---

## File Structure

- Create: `results/pictures/render_meg_global_logistics.py`
- Create: `results/pictures/meg-global-logistics.svg`
- Create: `results/pictures/meg-global-logistics.png`
- Reference style from: `results/pictures/render_meg_asia_consumption_change.py`
- Reference style from: `results/pictures/render_meg_global_consumption.py`

### Task 1: Build the data baseline and figure skeleton

**Files:**
- Create: `results/pictures/render_meg_global_logistics.py`

- [ ] **Step 1: Write the failing smoke check script command**

```bash
python "results/pictures/render_meg_global_logistics.py"
```

Expected: command fails with "No such file" before implementation.

- [ ] **Step 2: Create script skeleton with title, background, and output paths**

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

fig = plt.figure(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor("#efefef")

fig.text(0.03, 0.94, "3.2.4 全球MEG物流：区域流向", fontsize=28, fontweight="bold", color="#4a4a4a")
fig.lines.append(plt.Line2D([0.03, 0.98], [0.90, 0.90], transform=fig.transFigure, color="#4a4a4a", lw=2))
fig.lines.append(plt.Line2D([0.03, 0.12], [0.90, 0.90], transform=fig.transFigure, color="#c81d24", lw=4))
fig.text(0.92, 0.945, "CIEC", fontsize=24, fontweight="bold", color="#5a5a5a")

fig.savefig("results/pictures/meg-global-logistics.png", dpi=150, bbox_inches="tight")
fig.savefig("results/pictures/meg-global-logistics.svg", bbox_inches="tight")
```

- [ ] **Step 3: Add regional table data and flow edge data structures**

```python
region_rows = [
    ["中东", "净出口", "10", "东北亚/南亚/东南亚"],
    ["北美", "净出口", "2", "东北亚/西欧"],
    ["东北亚", "净进口", "7", "中东/北美"],
    ["南亚", "净进口", "3", "中东/东北亚"],
    ["西欧", "净进口", "2", "中东/北美"],
    ["东南亚", "近均衡", "1", "区内调配"],
    ["南美", "小幅进口", "1", "北美/中东"],
    ["非洲", "小幅进口", "1", "中东/西欧"],
]

flows = [
    ("中东", "东北亚", 3),
    ("中东", "南亚", 2),
    ("中东", "东南亚", 2),
    ("中东", "西欧", 1),
    ("北美", "东北亚", 1),
    ("北美", "西欧", 1),
    ("东北亚", "南亚", 1),
    ("东北亚", "东南亚", 1),
]
```

- [ ] **Step 4: Run script to verify files are generated**

Run: `python "results/pictures/render_meg_global_logistics.py"`
Expected: PASS with `meg-global-logistics.svg` and `meg-global-logistics.png` created.

- [ ] **Step 5: Commit skeleton and baseline data**

```bash
git add "results/pictures/render_meg_global_logistics.py"
git commit -m "feat: scaffold global MEG logistics figure with baseline flow data"
```

### Task 2: Implement table + map + flow rendering

**Files:**
- Modify: `results/pictures/render_meg_global_logistics.py`

- [ ] **Step 1: Write a failing visual completeness check**

Run: `python "results/pictures/render_meg_global_logistics.py"`
Expected: figure renders but missing at least one required module (table or map), so task not complete yet.

- [ ] **Step 2: Add top-left table module with fixed column widths**

```python
ax_table = fig.add_axes([0.05, 0.50, 0.46, 0.33])
ax_table.set_axis_off()
table = ax_table.table(
    cellText=region_rows,
    colLabels=["区域", "角色", "大致规模(Mt)", "主要流向/来源"],
    loc="center",
    cellLoc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.0, 1.35)
ax_table.text(0.5, 1.05, "全球MEG区域物流格局（2024，定性）", ha="center", va="bottom", fontsize=14)
```

- [ ] **Step 3: Add world-map-like region anchors and flow arrows**

```python
from matplotlib.patches import Ellipse, FancyArrowPatch

anchors = {
    "北美": (0.16, 0.30), "南美": (0.24, 0.17), "西欧": (0.44, 0.34), "非洲": (0.48, 0.22),
    "中东": (0.56, 0.30), "南亚": (0.64, 0.25), "东北亚": (0.76, 0.33), "东南亚": (0.70, 0.20),
}

ax_map = fig.add_axes([0.05, 0.08, 0.90, 0.36], facecolor="none")
ax_map.set_xlim(0, 1)
ax_map.set_ylim(0, 1)
ax_map.axis("off")

for name, (x, y) in anchors.items():
    ax_map.add_patch(Ellipse((x, y), 0.08, 0.05, facecolor="#d7dce1", edgecolor="#9aa3ad", lw=1.0))
    ax_map.text(x, y + 0.045, name, ha="center", va="bottom", fontsize=10, color="#404040")

width_map = {1: 1.2, 2: 2.0, 3: 2.8}
for src, dst, lvl in flows:
    x1, y1 = anchors[src]
    x2, y2 = anchors[dst]
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=10,
                            linewidth=width_map[lvl], color="#4f81bd", alpha=0.85,
                            connectionstyle="arc3,rad=0.15")
    ax_map.add_patch(arrow)
```

- [ ] **Step 4: Add bottom conclusions and source text with non-overlap spacing**

```python
fig.text(0.05, 0.035, "- 中东仍是全球MEG核心外供区，亚洲维持主要吸纳市场。", fontsize=16)
fig.text(0.05, 0.012, "- 北美与东北亚形成补充流向，欧洲进口以中东与北美为主。", fontsize=16)
fig.text(0.98, 0.004, "数据来源：Reuters、公开行业资讯、AI辅助整理（定性展示，非海关精算口径）", ha="right", fontsize=10, color="#666")
```

- [ ] **Step 5: Run script and verify full module presence**

Run: `python "results/pictures/render_meg_global_logistics.py"`
Expected: PASS with visible table + map + arrows + source note and no clipping.

- [ ] **Step 6: Commit full rendering logic**

```bash
git add "results/pictures/render_meg_global_logistics.py" "results/pictures/meg-global-logistics.svg" "results/pictures/meg-global-logistics.png"
git commit -m "feat: render template-style global MEG logistics map with regional table"
```

### Task 3: Validate style consistency and output quality

**Files:**
- Modify: `results/pictures/render_meg_global_logistics.py`
- Modify: `results/pictures/meg-global-logistics.svg`
- Modify: `results/pictures/meg-global-logistics.png`

- [ ] **Step 1: Write failing acceptance checklist before polish**

```text
Checklist:
1) 表格与地图两个模块都存在
2) 箭头不覆盖标题或底部数据来源
3) 与既有模板风格一致（灰底、红短线、CIEC、脚注）
```

Expected before polish: at least one item may fail due to overlap or spacing.

- [ ] **Step 2: Tune arrow size, curvature, and z-order to remove overlap**

```python
arrow = FancyArrowPatch(..., mutation_scale=8, zorder=3)
# 为高频流向单独设置 connectionstyle 的 rad 值，避免重叠
```

- [ ] **Step 3: Tune table and footer layout to eliminate clipping**

```python
ax_table = fig.add_axes([0.05, 0.51, 0.46, 0.32])
fig.text(0.98, 0.006, "数据来源：...", ha="right", fontsize=10)
```

- [ ] **Step 4: Run generation and output verification commands**

Run: `python "results/pictures/render_meg_global_logistics.py"`
Run: `ls "results/pictures"`
Expected: both `meg-global-logistics.svg` and `meg-global-logistics.png` present with latest timestamp.

- [ ] **Step 5: Commit final polish**

```bash
git add "results/pictures/render_meg_global_logistics.py" "results/pictures/meg-global-logistics.svg" "results/pictures/meg-global-logistics.png"
git commit -m "chore: polish MEG global logistics layout and readability"
```

## Plan Self-Review

- Spec coverage: all confirmed requirements are mapped (template style, table, world map, major routes, source note, outputs in `results/pictures`).
- Placeholder scan: no TODO/TBD placeholders remain.
- Type/signature consistency: one renderer script with consistent data structures (`region_rows`, `flows`, `anchors`) across tasks.
