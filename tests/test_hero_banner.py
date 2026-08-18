import os
import xml.etree.ElementTree as ET

def test_hero_banner():
    path = "assets/hero-banner.svg"
    assert os.path.exists(path), "Hero banner SVG must exist"
    tree = ET.parse(path)
    root = tree.getroot()
    assert root.tag.endswith("svg"), "Root element must be <svg>"
    text_content = "".join(root.itertext())
    assert "D. MEIRAM" in text_content
    assert "Staff AI & Distributed Systems Engineer" in text_content
    print("test_hero_banner PASSED!")

if __name__ == "__main__":
    test_hero_banner()
