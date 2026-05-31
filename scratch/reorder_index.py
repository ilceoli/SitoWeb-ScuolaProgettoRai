import re
import os

filepath = r"c:\Users\ilceo\Desktop\GitHub\SitoWeb-ScuolaProgettoRai\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. PARSE HTML CARDS
grid_match = re.search(r'(<div class="borghi-grid">)(.*?)(</div>\s*</div>\s*</section>)', content, re.DOTALL)
if not grid_match:
    print("Error: Could not match borghi-grid container")
    exit(1)

grid_header = grid_match.group(1)
grid_body = grid_match.group(2)
grid_footer = grid_match.group(3)

# Let's split grid_body by '<!--'
raw_chunks = grid_body.split("<!--")
cards = []
for chunk in raw_chunks:
    chunk = chunk.strip()
    if chunk:
        # Re-add the comment tag
        cards.append("<!-- " + chunk)

print(f"Parsed {len(cards)} cards in HTML")

completed_cards = []
in_lavorazione_cards = []

for card in cards:
    if "casignana.html" in card:
        # Clean Casignana title
        card = card.replace(" <br>(IN LAVORAZIONE)", "")
        card = card.replace(" (IN LAVORAZIONE)", "")
        completed_cards.append(card)
        print("Casignana card set to COMPLETED")
    elif "santagatadelbianco.html" in card:
        # Clean Sant'Agata title
        card = card.replace(" <br>(IN LAVORAZIONE)", "")
        card = card.replace(" (IN LAVORAZIONE)", "")
        completed_cards.append(card)
        print("Sant'Agata card set to COMPLETED")
    elif "IN LAVORAZIONE" in card:
        in_lavorazione_cards.append(card)
    else:
        completed_cards.append(card)

print(f"Completed HTML cards: {len(completed_cards)}")
print(f"In Lavorazione HTML cards: {len(in_lavorazione_cards)}")

new_grid_body = "\n\n          ".join(completed_cards) + "\n\n          " + "\n\n          ".join(in_lavorazione_cards)
old_grid_block = grid_match.group(0)
new_grid_block = grid_header + "\n          " + new_grid_body + "\n        " + grid_footer

# 2. PARSE JS ARRAY
js_match = re.search(r'(var borghi = \[)(.*?)(\];)', content, re.DOTALL)
if not js_match:
    print("Error: Could not find var borghi array in JS")
    exit(1)

js_header = js_match.group(1)
js_body = js_match.group(2)
js_footer = js_match.group(3)

# Parse JS objects inside the array by matching { ... } with recursive balance or clean non-greedy
objects = re.findall(r'(\{\s*nome:\s*[^}]+?\s*\})', js_body, re.DOTALL)
print(f"Parsed {len(objects)} objects in JS array")

completed_names = [
    "IIS G. Marconi", "IPSIA Siderno", "IPSIA Locri", # Scuole (always completed/first)
    "Valle delle Grandi Pietre", "Villa Romana del Naniglio", "Gerace", "Brancaleone", "San Luca",
    "Locri", "Bianco", "Samo", "Siderno", "Caulonia", "Sant'Agata del Bianco", "Casignana"
]

scuole_js = []
completed_js = []
in_lavorazione_js = []

for obj in objects:
    name_match = re.search(r'nome:\s*(?:"([^"]*)"|\'([^\']*)\')', obj)
    if name_match:
        name = name_match.group(1) or name_match.group(2)
        # Check if school
        if "IIS G. Marconi" in name or "IPSIA Siderno" in name or "IPSIA Locri" in name:
            scuole_js.append(obj)
        else:
            is_completed = False
            for cn in completed_names:
                if cn.lower() in name.lower():
                    is_completed = True
                    break
            if is_completed:
                completed_js.append(obj)
            else:
                in_lavorazione_js.append(obj)
    else:
        print(f"Warning: Could not parse name from JS object: {obj}")

print(f"Schools JS: {len(scuole_js)}")
print(f"Completed JS: {len(completed_js)}")
print(f"In Lavorazione JS: {len(in_lavorazione_js)}")

# Reassemble JS array body
new_js_body = "\n      // SCUOLE\n      " + ",\n      ".join(scuole_js) + ",\n\n      // BORGHI COMPLETATI\n      " + ",\n      ".join(completed_js) + ",\n\n      // BORGHI IN LAVORAZIONE\n      " + ",\n      ".join(in_lavorazione_js) + "\n    "

old_js_block = js_match.group(0)
new_js_block = js_header + new_js_body + js_footer

content_replaced = content.replace(old_grid_block, new_grid_block)
content_replaced = content_replaced.replace(old_js_block, new_js_block)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content_replaced)

print("Reordering in index.html completed successfully!")
