import os
import re

borghi_dir = r"c:\Users\ilceo\Desktop\GitHub\SitoWeb-ScuolaProgettoRai\assets\borghi"

logo_patterns = []
for root, dirs, files in os.walk(borghi_dir):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            # Find logo div content
            match = re.search(r'<div class="logo">.*?</div>', content, re.DOTALL)
            if match:
                print(f"File: {f}")
                print(match.group(0))
                print("-" * 40)
