# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

def main():
    fig = plt.figure(figsize=(16, 9), dpi=200)
    fig.patch.set_facecolor("#f4f5f7")
    
    # Title
    fig.text(0.04, 0.90, "中国EG行业成本梯度曲线 - 具体装置名单（2025-2026）", fontsize=28, fontweight="bold", color="#2c3e50")
    fig.text(0.04, 0.85, "说明：基于公开工艺特征与区域优势划分的成本梯队（示意性归类，非确切装置财报成本）", fontsize=14, color="#7f8c8d")
    
    # Left Table Background Area (0.04 to 0.69)
    table_bg = FancyBboxPatch((0.04, 0.22), 0.65, 0.58, boxstyle="round,pad=0.01,rounding_size=0.01", 
                              facecolor="#ffffff", edgecolor="#bdc3c7", linewidth=1)
    fig.patches.append(table_bg)

    ax_table = fig.add_axes([0.04, 0.22, 0.65, 0.58])
    ax_table.axis('off')
    
    columns = ["成本梯队", "工艺类型", "代表装置/企业", "产能\n(万吨/年)", "位置", "当前运行状态", "出清风险"]
    data = [
        ["第一梯队\n(基荷优势)", "大炼化一体化", "镇海、恒力、荣盛等\n沿海大炼化", "80-100", "沿海七大基地", "满负荷/高负荷运行", "极低"],
        ["第二梯队\n(资源优势)", "高效/新型煤制", "陕煤、大宁等大型\n现代煤化工项目", "40-60", "陕西/内蒙/新疆", "较高负荷运行\n(视煤价波动)", "较低"],
        ["第三梯队\n(边际产能)", "外采乙烯/\n一般煤制", "华东外采法、华中/\n华北部分中型煤制", "20-40", "华东沿海/华北", "弹性调节负荷\n(随加工费启停)", "中等\n(利润挤压区)"],
        ["第四梯队\n(高危产能)", "老旧小装置/\n合成气", "早期投产的老旧装置/\n技术受限的小装置", "<20", "分散(华中/西南)", "长期停车/低负荷\n面临技改或淘汰", "高\n(实质性出清)"]
    ]
    
    # Matching gray/business report colors (instead of bright pastels)
    colors = ["#eef2f5", "#fdfbf7", "#fdf7f4", "#fbeeee"]
    header_color = "#d9e1e8"
    
    # Use pyplot table
    table = ax_table.table(cellText=data, colLabels=columns, loc='center', cellLoc='center',
                           colWidths=[0.12, 0.14, 0.22, 0.10, 0.14, 0.16, 0.12])
    
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 4.2)
    
    # Style the table
    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        row, col = key
        
        # Border
        cell.set_edgecolor('#ecf0f1')
        cell.set_linewidth(1.5)
        
        # Row colors
        if row == 0:  # Header
            cell.set_facecolor(header_color)
            cell.set_text_props(weight='bold', color='#2c3e50', fontsize=13)
        else:
            cell.set_facecolor(colors[row - 1])
            cell.set_text_props(color='#34495e')
            
            if col == 0: # Bold the first column
                cell.set_text_props(weight='bold', color='#2c3e50')
                
            if col == 6: # Color code risk
                risk_colors = ["#27ae60", "#f39c12", "#d35400", "#c0392b"]
                cell.set_text_props(color=risk_colors[row - 1], weight='bold')

    # Right Chart Background Area (0.72 to 0.96)
    chart_bg = FancyBboxPatch((0.72, 0.22), 0.24, 0.58, boxstyle="round,pad=0.01,rounding_size=0.01", 
                              facecolor="#ffffff", edgecolor="#bdc3c7", linewidth=1)
    fig.patches.append(chart_bg)

    ax_chart = fig.add_axes([0.76, 0.30, 0.17, 0.43])
    ax_chart.set_facecolor("#ffffff")
    
    cost_levels = [3500, 4200, 4800, 5600]
    labels = ["梯队一", "梯队二", "梯队三", "梯队四"]
    x_pos = np.arange(len(labels))
    
    # Bar chart to simulate cost curve ladder
    bars = ax_chart.bar(x_pos, cost_levels, width=0.7, color=colors, edgecolor="#bdc3c7", linewidth=1.5)
    
    ax_chart.set_ylim(0, 6500)
    ax_chart.set_ylabel("预估现金成本相对水平", fontsize=9.5, color='#7f8c8d', labelpad=6)
    ax_chart.set_xticks(x_pos)
    ax_chart.set_xticklabels(labels, fontsize=10.5, fontweight='bold', color='#2c3e50')
    ax_chart.spines['top'].set_visible(False)
    ax_chart.spines['right'].set_visible(False)
    ax_chart.spines['left'].set_color('#bdc3c7')
    ax_chart.spines['bottom'].set_color('#bdc3c7')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.5, color='#bdc3c7')
    
    # Add market price line
    ax_chart.axhline(4500, color='#e74c3c', linestyle='--', linewidth=2, alpha=0.8)
    ax_chart.text(3.28, 5750, '价格中枢\n(承压线)', color='#e74c3c', fontsize=10, ha='right', va='bottom')
    
    # Value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax_chart.text(bar.get_x() + bar.get_width()/2., height - 520,
                f"成本\n指数",
                ha='center', va='bottom', fontsize=9, color='#7f8c8d')

    # Add a marginal cost line connecting the tops
    ax_chart.plot(x_pos, cost_levels, color='#34495e', marker='o', linewidth=2.5, markersize=8)

    # Chart title
    fig.text(0.84, 0.76, "成本梯度示意 (现金流出清压力)", fontsize=12.5, fontweight='bold', color='#2c3e50', ha='center')

    # Bottom Summary Box
    summary_box = FancyBboxPatch((0.04, 0.05), 0.92, 0.12, boxstyle="round,pad=0.015,rounding_size=0.015", 
                                 facecolor="#ffffff", edgecolor="#bdc3c7", linewidth=1)
    fig.patches.append(summary_box)
    
    fig.text(0.06, 0.115, "核心结论 (Core Takeaways):", fontsize=14, fontweight="bold", color="#e74c3c")
    fig.text(0.06, 0.072, "1. 第一梯队（大炼化）凭借极低成本形成基荷供应，抗风险能力最强；\n"
                          "2. 第三、第四梯队主要由外采乙烯及老旧煤制构成，是未来1-2年出清和降负荷的主要来源。",
             fontsize=11.8, color="#34495e", linespacing=1.55)
             
    fig.text(0.95, 0.02, "CIEC", fontsize=18, fontweight="bold", color="#95a5a6", ha="right")
    
    plt.savefig("results/pictures/eg_cost_ladder_ppt.png", dpi=200, bbox_inches="tight")
    plt.savefig("results/pictures/eg_cost_ladder_ppt.svg", bbox_inches="tight")
    print("Files saved successfully to results/pictures/eg_cost_ladder_ppt.*")

if __name__ == "__main__":
    main()
