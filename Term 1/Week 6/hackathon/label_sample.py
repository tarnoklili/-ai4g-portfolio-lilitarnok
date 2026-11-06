"""Step 1 of your honest test: draw 50 random items for YOU to label.

The model's answers are deliberately left out, so they cannot influence you.
Run this after the collector has gathered a good number of items:
    python label_sample.py
Then open data/to_label.csv in Excel / Sheets and fill the 'my_label' column with
exactly one of: negative, neutral, positive.   Save it as CSV.
"""
import csv
import random
from pathlib import Path

SRC = Path("data/items.csv")
OUT = Path("data/to_label.csv")
N = 50

if OUT.exists():
    raise SystemExit(f"{OUT} already exists. Delete it first if you really want a new sample.")

with SRC.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
if len(rows) < N:
    raise SystemExit(f"Only {len(rows)} items collected so far, need at least {N}.")

random.seed(42)
sample = random.sample(rows, N)
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["item_id", "text", "my_label"])
    for r in sample:
        w.writerow([r["item_id"], r["text"], ""])
print(f"Wrote {OUT} with {N} items. Fill in the my_label column.")
