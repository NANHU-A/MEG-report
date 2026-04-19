# MEG Defense Speech Draft Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a 35-42 minute defense speech markdown that maps to substantive pages of `MEG_report(3.1).md`, with emphasis on supply, demand, logistics, inventory, and profit.

**Architecture:** Build the script in one deliverable file under `presentation/`, using a fixed per-page template and weighted timing tiers. The script follows a single narrative spine: supply -> demand -> logistics -> inventory -> profit -> price transmission explanation -> conditional trading mapping.

**Critical China section requirement:** In China supply-demand chapters, import/export content and logic are mandatory. The script must explicitly explain import dependency, source-country structure, logistics/geopolitical risks, export reality, and how these factors transmit to domestic inventory and profit.

**Tech Stack:** Markdown authoring, repository file review via Read, directory creation via PowerShell, patch-based file writing.

---

### Task 1: Create output location and script scaffold

**Files:**
- Create: `presentation/MEG_defense_speech_v1.md`
- Modify: `docs/superpowers/plans/2026-04-16-meg-defense-speech-plan.md`

- [ ] **Step 1: Verify root directories and report source exist**

Run: `Get-ChildItem`
Expected: includes `results/`, `docs/`, and no blocking path issues.

- [ ] **Step 2: Create `presentation/` directory if missing**

Run: `if (!(Test-Path "presentation")) { New-Item -ItemType Directory -Path "presentation" | Out-Null }`
Expected: `presentation/` exists.

- [ ] **Step 3: Write script file scaffold with sections**

Insert markdown headings:

```md
# MEG答辩逐页讲稿（v1）
## 使用说明
## 全局时间分配
## 逐页讲稿
## Q&A备答清单
```

- [ ] **Step 4: Verify scaffold write success**

Run: `Get-Item "presentation/MEG_defense_speech_v1.md"`
Expected: file exists and is readable.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/plans/2026-04-16-meg-defense-speech-plan.md presentation/MEG_defense_speech_v1.md
git commit -m "docs: scaffold MEG defense speech implementation plan"
```

### Task 2: Build weighted substantive-page speech content

**Files:**
- Modify: `presentation/MEG_defense_speech_v1.md`

- [ ] **Step 1: Write Tier-1 pages (high-weight pages)**

Cover pages:

```text
2, 4, 9, 12, 13, 21, 24, 28, 29, 30, 41, 44, 47, 48
```

Each page must include:

```md
### Page X（建议时长）
- 页面定位：
- 台上讲稿：
- 一句话结论：
- 若被追问：
```

- [ ] **Step 2: Write Tier-2 pages (medium-weight pages)**

Cover pages:

```text
5, 8, 10, 14, 16, 18, 19, 22, 25, 27, 31, 35, 36, 37, 43
```

Use shorter script body, but keep same four-field structure.

- [ ] **Step 2.5: Add dedicated China import/export logic in relevant pages**

Must explicitly strengthen pages:

```text
24 (进口依存度), 25-27 (进口/出口结构), 41 (供需平衡), 47 (交易标的)
```

Each of these pages must include:

```text
进口/出口事实 -> 物流与地缘约束 -> 对港口库存与利润的传导 -> 对交易节奏含义
```

- [ ] **Step 3: Write Tier-3 concise bridge pages**

Add concise bridge content for remaining substantive pages with 15-35 seconds pacing.

- [ ] **Step 4: Verify all script pages remain inside narrative spine**

Run checklist in file:

```text
Each page states: what changed -> why -> inventory/profit impact -> trading implication.
```

- [ ] **Step 5: Commit**

```bash
git add presentation/MEG_defense_speech_v1.md
git commit -m "docs: add weighted page-by-page MEG defense speech"
```

### Task 3: Add data-storytelling and risk-conditioned trading language

**Files:**
- Modify: `presentation/MEG_defense_speech_v1.md`

- [ ] **Step 1: Inject chapter-level storytelling arc**

For each chapter, enforce:

```text
背景 -> 矛盾 -> 证据 -> 结论 -> 动作
```

- [ ] **Step 2: Inject conditional trading trigger wording**

Add explicit patterns:

```text
偏多触发 / 偏空触发 / 中性观望 + 证伪条件 + 风险提示
```

- [ ] **Step 3: Add a dedicated “价格传导逻辑说明” paragraph**

Include:

```text
成本端、物流端、库存端、利润端如何传导到价格，不做绝对点位预测。
```

- [ ] **Step 4: Validate speech tone for industrial + trading panel**

Manual check: avoid student narration and avoid over-academic detours.

- [ ] **Step 5: Commit**

```bash
git add presentation/MEG_defense_speech_v1.md
git commit -m "docs: refine MEG speech with storytelling and conditional trade logic"
```

### Task 4: Complete Q&A appendix and final quality checks

**Files:**
- Modify: `presentation/MEG_defense_speech_v1.md`

- [ ] **Step 1: Add 10-15 high-frequency defense Q&A items**

Must prioritize:

```text
供应、需求、物流、库存、利润、中国进出口逻辑、进口依存、地缘风险、交易触发失效条件
```

- [ ] **Step 2: Run content completeness checks**

Run:

```bash
rg "^### Page" presentation/MEG_defense_speech_v1.md
```

Expected: substantive pages are covered with explicit section headers.

- [ ] **Step 3: Run style checks manually**

Checklist:

```text
No TODO/TBD placeholders
All page sections include one-sentence conclusion
Primary focus remains supply-demand-logistics-inventory-profit
```

- [ ] **Step 4: Final save and verification read**

Run: `Get-Content "presentation/MEG_defense_speech_v1.md"`
Expected: complete readable markdown with no broken headings.

- [ ] **Step 5: Commit**

```bash
git add presentation/MEG_defense_speech_v1.md
git commit -m "docs: finalize MEG defense speech and Q&A appendix"
```
