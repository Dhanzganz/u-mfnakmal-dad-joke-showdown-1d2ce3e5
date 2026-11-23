"""Dad Joke Showdown entry.

Writes the competition entry — a dad joke about a developer who went
broke because he used up all his cache — to /output/entry.txt with no
trailing newline.
"""

import os

ENTRY = "Why did the developer go broke? Because he used up all his cache."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
