import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import textwrap

# Font settings for high-quality Chinese rendering
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

def create_slide():
    # Setup 16:9 Figure
    fig = plt.figure(figsize=(16, 9), dpi=200, facecolor="#f5f7fa")
    
    # Background pattern
    ax_bg = fig.add_axes([0, 0, 1, 1], zorder=-1)
    ax_bg.set_axis_off()
    
    # Subtle molecular/marble-like blobs
    blobs = [
        (0.85, 0.85, 0.4, 0.3, "#e2e6eb", 20),
        (0.15, 0.15, 0.5, 0.4, "#e8ecf1", -15),
        (0.6, 0.3, 0.3, 0.25, "#dde3eb", 45),
    ]
    for x, y, w, h, color, angle in blobs:
        ellipse = patches.Ellipse((x, y), w, h, angle=angle, facecolor=color, alpha=0.6, transform=ax_bg.transAxes)
        ax_bg.add_patch(ellipse)

    # Title Area
    fig.text(0.05, 0.90, "全球供给：MEG投产与退出趋势", fontsize=32, fontweight='bold', color="#112a46")
    fig.text(0.05, 0.86, "2024-2025年主要新增产能与边际退出产能梳理（万吨/年）", fontsize=16, color="#4a5f78")
    
    # Top blue accent line
    fig.add_artist(patches.Rectangle((0.05, 0.96), 0.9, 0.01, facecolor="#1a5276", transform=fig.transFigure, clip_on=False))

    def wrap_cell_text(s: str, width: int) -> str:
        s = str(s)
        # Prefer breaking on Chinese punctuation/semicolons for readability.
        s = s.replace("；", "；\n").replace("。", "。\n").replace("→", "→ ")
        lines = []
        for part in s.split("\n"):
            part = part.strip()
            if not part:
                continue
            lines.extend(textwrap.wrap(part, width=width, break_long_words=True, break_on_hyphens=False) or [part])
        return "\n".join(lines)

    # Table Area (make it larger on the slide)
    ax_table = fig.add_axes([0.045, 0.22, 0.73, 0.62])
    ax_table.axis('off')

    # Data (as specified)
    col_labels = [
        "地区",
        "投产趋势\n（2025-2027）",
        "退出/优化趋势\n（2025-2027）",
        "主要工艺影响",
        "定性判断\n（成本曲线位置）",
    ]
    table_data = [
        ["中国", "新增放缓（150-250万吨/年），民营大炼化一体化油制为主", "高成本小型煤制 + 老旧/非一体化油制加速退出", "石脑油制（一体化）+合成气制存量优化", "中低成本区稳定；高成本区出清"],
        ["中东", "稳健新增，低成本乙烷制扩能为主", "少量老旧装置优化", "乙烷制（气头）主导", "最左端低成本基荷"],
        ["北美", "温和扩能，依托页岩气乙烷优势", "极少，重点升级", "乙烷制为主", "低成本区，出口导向"],
        ["亚洲（日韩/台湾）", "新增极少", "老旧非一体化油制持续停车/退出", "传统园区油制（石脑油制）", "中高成本区 → 右端退出"],
        ["欧洲", "基本无新增", "老旧装置理性化退出或转产", "石脑油制为主", "高成本区，逐步退出"],
    ]

    # Wrap cell text to avoid overlap
    wrap_widths = [10, 20, 20, 16, 18]
    wrapped_table_data = []
    for row in table_data:
        wrapped_row = []
        for idx, val in enumerate(row):
            wrapped_row.append(wrap_cell_text(val, wrap_widths[idx]))
        wrapped_table_data.append(wrapped_row)

    # Create Table
    table = ax_table.table(
        cellText=wrapped_table_data,
        colLabels=col_labels,
        loc='center',
        cellLoc='center',
        colWidths=[0.12, 0.23, 0.23, 0.18, 0.24],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(11.0)
    table.scale(1.0, 2.55)

    # Style Table
    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor('#d3dae1')
        cell.PAD = 0.02
        if i == 0:
            cell.set_facecolor('#24527a')
            cell.set_text_props(color='white', weight='bold', fontsize=12.0)
        elif i % 2 == 0:
            cell.set_facecolor('#eef2f5')
        else:
            cell.set_facecolor('#ffffff')
            
        if i > 0:
            # Left align text-heavy columns to avoid visual crowding
            if j in (1, 2, 3, 4):
                cell.set_text_props(fontsize=10.2, ha='left', va='center')
            else:
                cell.set_text_props(fontsize=10.4)

    # Right Red-Accent Callout
    # Right callout (keep margin, avoid text overflow)
    ax_callout = fig.add_axes([0.785, 0.30, 0.19, 0.47])
    ax_callout.axis('off')
    
    callout_box = patches.FancyBboxPatch(
        (0, 0), 1, 1, boxstyle="round,pad=0.05",
        facecolor="#fff0f0", edgecolor="#c0392b", linewidth=2, transform=ax_callout.transAxes
    )
    ax_callout.add_patch(callout_box)
    
    # Manually hard-wrap to avoid overflow (CJK auto-wrap is unreliable in Matplotlib)
    callout_text = (
        "边际成本曲线驱动：\n"
        "低成本区（气头+一体化油制）\n"
        "维持扩张；\n"
        "高成本区（老旧/小型装置）\n"
        "加速退出 →\n"
        "全球负荷偏低\n"
        "（60-65%）"
    )
    ax_callout.text(
        0.06,
        0.90,
        callout_text,
        fontsize=10.8,
        color="#333333",
        verticalalignment='top',
        fontweight='normal',
        linespacing=1.4,
        wrap=False,
        clip_on=True,
    )
    
    # Red accent ribbon on callout
    ax_callout.add_patch(patches.Rectangle((0, 0.2), 0.03, 0.6, facecolor="#c0392b", transform=ax_callout.transAxes))

    # Bold Bottom Summary
    summary_bg = patches.Rectangle((0.05, 0.12), 0.9, 0.08, facecolor="#24527a", transform=fig.transFigure)
    fig.add_artist(summary_bg)
    fig.text(0.5, 0.16, "全球MEG投产与退出呈现明显分化，低成本气头与一体化油制维持扩张，高成本老旧产能加速出清，行业转向成本优化与结构调整。",
             fontsize=15.5, color="white", fontweight='bold', ha='center', va='center')

    # Data Source Line
    fig.text(0.05, 0.05, "数据来源：CCF（2025聚酯产业市场年度报告）、卓创资讯、百川盈孚、S&P Global（2025-2026数据）", fontsize=10, color="#7f8c8d")
    fig.text(0.85, 0.05, "机密 ★ 仅供内部参考", fontsize=10, color="#7f8c8d", ha='right')

    # Save Output
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    png_path = os.path.join(output_dir, "meg_global_supply_trend.png")
    svg_path = os.path.join(output_dir, "meg_global_supply_trend.svg")
    
    plt.savefig(png_path, bbox_inches='tight', pad_inches=0.1)
    plt.savefig(svg_path, bbox_inches='tight', pad_inches=0.1, format='svg')
    print(f"Saved: {png_path}")
    print(f"Saved: {svg_path}")

if __name__ == "__main__":
    create_slide()
