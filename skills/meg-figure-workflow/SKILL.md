---
name: meg-figure-workflow
description: Use when creating or iterating MEG report figures in this project, especially when reproducing template style into SVG and PNG outputs under results/pictures.
---

# MEG Figure Workflow

## Overview
This skill standardizes the workflow used for the 5 completed figures in `results/pictures`.
Core principle: lock template style first, then iterate only data/layout until no overlap or clipping.

## When To Use
- Build a new MEG report chart from a reference image.
- Rework an existing chart to match template style.
- Produce final `SVG + PNG` assets for PPT/report insertion.

## Proven 5-Image Baseline
The workflow is derived from these generated assets:
- `results/pictures/eg-industry-chain.svg`
- `results/pictures/eg-supply-demand-indicators.svg`
- `results/pictures/meg-global-consumption-structure.svg`
- `results/pictures/meg-asia-consumption-change.svg`
- `results/pictures/meg-global-logistics.svg`

## Standard Process
1. Confirm output target and filename in `results/pictures`.
2. Mirror template chrome first: gray background, title line, red short line, CIEC mark.
3. Build layout skeleton (axes blocks and spacing) before detailed data.
4. Fill chart/table data with practical industry estimates when exact data is unavailable.
5. Add world-map/background watermark only after readability is confirmed.
6. Tune arrows/labels/legend for non-overlap (line width, marker size, arc curvature, zorder).
7. Export both formats from one script run:
   - `results/pictures/<name>.png`
   - `results/pictures/<name>.svg`
8. Validate final chart checklist:
   - required modules present
   - no overlap/clipping
   - style consistent with existing deck

## Data Handling Rules
- Prefer recent public sources and coarse quantitative bands if precision is not required.
- When collecting or refreshing data during charting, use the latest available point up to **2025** by default.
- Mark estimates clearly in the source note.
- Keep units explicit (`万吨`, `%`, etc.).

## Styling Defaults
- Fonts: `Microsoft YaHei`, `SimHei`, `Noto Sans CJK SC`, `Arial Unicode MS`.
- Background: `#efefef`.
- Header line: dark gray full line + red short segment.
- Keep arrow thickness in 3 visible levels when flow grades are required.

## Common Fixes
- **Arrow overlap:** lower `mutation_scale`, split `rad` values, stagger endpoints.
- **Footer conflict:** move source text down and legend up.
- **Table crowding:** reduce font or widen grouped columns, simulate merged cells with hidden inner borders.
- **Map not visible:** use explicit map axis facecolor contrast and stronger continent fill.
