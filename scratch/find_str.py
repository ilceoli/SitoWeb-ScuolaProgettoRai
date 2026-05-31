import re

filepath = r"c:\Users\ilceo\Desktop\GitHub\SitoWeb-ScuolaProgettoRai\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

matches = [m.start() for m in re.finditer("Sant'Agata del Bianco", content)]
print(f"Found {len(matches)} matches:")
for idx in matches:
    print(content[idx:idx+150])
