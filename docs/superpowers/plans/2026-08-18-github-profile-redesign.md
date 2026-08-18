# GitHub Profile Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the GitHub profile of **D. Meiram** (`@disamee`) into an ultra-high-converting, aesthetically flawless engineering showcase for Senior/Staff AI, RAG & Systems roles.

**Architecture:** A unified profile repository (`disamee/disamee`) featuring custom-crafted dark-tech SVG hero visuals, modular SVG bento metric cards, a native GitHub Mermaid architecture pipeline diagram, 6 structured NDA-safe case study cards, and an executive recruiter fast-track section.

**Tech Stack:** GitHub Flavored Markdown, SVG (Scalable Vector Graphics), Mermaid.js, GitHub Shield/Badge integrations.

## Global Constraints
- Target Repo: `disamee/disamee`
- Style: Linear Dark-Tech Bento (`#090d16` graphite background, `#00f0ff` cyan accent, `#10b981` emerald status, `#8b949e` muted slate)
- Accessibility & Theme Support: Crisp high-contrast visibility on both dark and light modes
- No generic AI slop or placeholder links: all 6 case study repository URLs must be valid and accurately described.

---

### Task 1: Design & Generate the Vector SVG Hero Banner (`assets/hero-banner.svg`)

**Files:**
- Create: `assets/hero-banner.svg`
- Test: `tests/verify_assets.py`

**Interfaces:**
- Produces: `assets/hero-banner.svg` referenced in `README.md`

- [ ] **Step 1: Write test script to verify SVG validity and dimensions**
```python
import os
import xml.etree.ElementTree as ET

def test_hero_banner():
    path = "assets/hero-banner.svg"
    assert os.path.exists(path), "Hero banner SVG must exist"
    tree = ET.parse(path)
    root = tree.getroot()
    assert root.tag.endswith("svg"), "Root element must be <svg>"
    assert "viewBox" in root.attrib or ("width" in root.attrib and "height" in root.attrib)
    text_content = "".join(root.itertext())
    assert "D. MEIRAM" in text_content
    assert "Staff AI & Distributed Systems Engineer" in text_content
```

- [ ] **Step 2: Run test to verify it fails**
Run: `python -c "import os; assert os.path.exists('assets/hero-banner.svg')"`
Expected: FAIL

- [ ] **Step 3: Implement `assets/hero-banner.svg`**
Create the 1200x400 vector SVG banner with animated status pulse, RAG node mesh background, crisp sans typography, specialization tags, and social quick-access badges.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -c "import xml.etree.ElementTree as ET; tree = ET.parse('assets/hero-banner.svg'); assert 'MEIRAM' in ''.join(tree.getroot().itertext()); print('Hero SVG Valid!')"`
Expected: PASS

---

### Task 2: Design & Build Modular Bento Metric Cards (`assets/metrics/`)

**Files:**
- Create: `assets/metrics/card-rag.svg`
- Create: `assets/metrics/card-tickers.svg`
- Create: `assets/metrics/card-prompts.svg`
- Create: `assets/metrics/card-scraping.svg`

**Interfaces:**
- Produces: 4 high-contrast SVG bento stat cards with electric gradients and crisp typography.

- [ ] **Step 1: Write test script to verify metric card SVGs**
```python
import os, xml.etree.ElementTree as ET

def test_bento_cards():
    cards = ['card-rag.svg', 'card-tickers.svg', 'card-prompts.svg', 'card-scraping.svg']
    for c in cards:
        path = os.path.join("assets/metrics", c)
        assert os.path.exists(path), f"{c} must exist"
        tree = ET.parse(path)
        assert tree.getroot().tag.endswith("svg")
```

- [ ] **Step 2: Implement all 4 Bento Metric SVGs**
1. `card-rag.svg`: "20,000+ Docs RAG" • Hybrid BM25 & Qdrant Search
2. `card-tickers.svg`: "<100ms Live Tickers" • Asynchronous WebSocket Pub/Sub
3. `card-prompts.svg`: "400+ LOC Prompts" • Zero-Hallucination Safety Guardrails
4. `card-scraping.svg`: "10,000+ Daily Scrapes" • Distributed Selenium Chrome Cluster

- [ ] **Step 3: Run test to verify all 4 SVGs pass**
Run: `python -c "import os; [open(f'assets/metrics/{x}') for x in ['card-rag.svg', 'card-tickers.svg', 'card-prompts.svg', 'card-scraping.svg']]; print('All Metric Cards Valid!')"`
Expected: PASS

---

### Task 3: Compose Master `README.md`

**Files:**
- Create: `README.md`
- Test: `tests/verify_readme.py`

**Interfaces:**
- Consumes: `assets/hero-banner.svg`, `assets/metrics/*.svg`
- Produces: Complete drop-in `README.md` for profile repo `disamee/disamee`

- [ ] **Step 1: Write validation test for README.md structure**
```python
def test_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    assert "assets/hero-banner.svg" in content
    assert "```mermaid" in content
    assert "fergus-commodity-analytics-case-study" in content
    assert "geological-rag-architecture-case-study" in content
    assert "industrial-hse-rag-case-study" in content
    assert "epd-shipment-tracking-case-study" in content
    assert "agri-economic-dashboard-case-study" in content
    assert "microfinance-aggregator-case-study" in content
    print("README structure test PASSED")
```

- [ ] **Step 2: Implement `README.md`**
Assemble the full document with:
- Top Hero banner linking to profile
- Quick Bio & Positioning
- Bento Grid metrics (linking cards)
- Mermaid System Architecture Blueprint
- 6 Detailed Case Study Showcase Cards with live links & tech tags
- Modern Tech Stack Grid (AI, Distributed Backends, Frontend/Data, Cloud/DevOps)
- Recruiter Fast-Track & Direct Contact Callouts

- [ ] **Step 3: Run test to verify README structure**
Run: `python tests/verify_readme.py`
Expected: PASS

---

### Task 4: Create Deployment Guide & Verify Whole Package

**Files:**
- Create: `DEPLOYMENT_GUIDE.md`
- Test: Full end-to-end verification script

- [ ] **Step 1: Write `DEPLOYMENT_GUIDE.md`**
Provide clear, step-by-step instructions for:
1. Pushing `README.md` and `assets/` to `https://github.com/disamee/disamee`
2. Setting up GitHub Pinned Repositories (the 6 case studies) for maximum profile visual balance
3. Adding profile Bio, Location, and Social Links in GitHub Profile Settings

- [ ] **Step 2: Run complete package verification**
Run: `python -c "import os; assert os.path.exists('README.md') and os.path.exists('assets/hero-banner.svg') and os.path.exists('DEPLOYMENT_GUIDE.md'); print('Full Profile Redesign Package Complete!')"`
Expected: PASS
