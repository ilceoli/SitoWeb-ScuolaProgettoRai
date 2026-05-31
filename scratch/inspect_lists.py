import re
import os

filepath = r"c:\Users\ilceo\Desktop\GitHub\SitoWeb-ScuolaProgettoRai\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

grid_match = re.search(r'(<div class="borghi-grid">)(.*?)(</div>\s*</div>\s*</section>)', content, re.DOTALL)
grid_body = grid_match.group(2)

raw_chunks = grid_body.split("<!--")
cards = []
for chunk in raw_chunks:
    chunk = chunk.strip()
    if chunk:
        cards.append("<!-- " + chunk)

for idx, card in enumerate(cards):
    title_match = re.search(r'<h3>(.*?)</h3>', card)
    title = title_match.group(1).replace('\n', ' ') if title_match else "No Title"
    has_lavorazione = "IN LAVORAZIONE" in card
    has_casignana = "casignana.html" in card
    print(f"Card {idx}: '{title}' | Lavorazione={has_lavorazione} | Casignana={has_casignana}")
