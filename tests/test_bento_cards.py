import os
import xml.etree.ElementTree as ET

def test_bento_cards():
    cards = ['card-rag.svg', 'card-tickers.svg', 'card-prompts.svg', 'card-scraping.svg']
    for c in cards:
        path = os.path.join("assets/metrics", c)
        assert os.path.exists(path), f"{c} must exist"
        tree = ET.parse(path)
        assert tree.getroot().tag.endswith("svg"), f"{c} must be valid SVG"
    print("test_bento_cards PASSED!")

if __name__ == "__main__":
    test_bento_cards()
