import os

def test_readme():
    path = "README.md"
    assert os.path.exists(path), "README.md must exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "assets/hero-banner.svg" in content, "Must reference hero banner"
    assert "assets/metrics/card-rag.svg" in content, "Must reference bento cards"
    assert "```mermaid" in content, "Must include native Mermaid diagram"
    assert "fergus-commodity-analytics-case-study" in content
    assert "geological-rag-architecture-case-study" in content
    assert "industrial-hse-rag-case-study" in content
    assert "epd-shipment-tracking-case-study" in content
    assert "agri-economic-dashboard-case-study" in content
    assert "microfinance-aggregator-case-study" in content
    assert "D. Meiram" in content or "D. MEIRAM" in content
    print("test_readme PASSED!")

if __name__ == "__main__":
    test_readme()
