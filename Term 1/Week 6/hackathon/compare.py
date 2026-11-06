"""Step 2 of your honest test: compare YOUR labels with cardiffnlp and VADER.

Needs:  pip install vaderSentiment
Run:    python compare.py
Output: data/test_table.csv  (your 50 labels, both models' output, where they disagree)
"""
import csv
import io
from collections import Counter
from pathlib import Path

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

ITEMS = Path("data/items.csv")
LABELED = Path("data/to_label.csv")
OUT = Path("data/test_table.csv")
VALID = {"negative", "neutral", "positive"}


def vader_label(analyzer, text):
    """Standard VADER thresholds: compound >= 0.05 positive, <= -0.05 negative."""
    c = analyzer.polarity_scores(text)["compound"]
    return "positive" if c >= 0.05 else "negative" if c <= -0.05 else "neutral"


with ITEMS.open(newline="", encoding="utf-8") as f:
    cardiff = {r["item_id"]: r["label"].strip().lower() for r in csv.DictReader(f)}

def read_labeled(path):
    """Read the labelled file whether it came from Google Sheets (comma, UTF-8)
    or from Dutch Excel (semicolon, sometimes Windows-1252 and/or a BOM)."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")
    header = text.splitlines()[0]
    delim = ";" if header.count(";") > header.count(",") else ","
    return list(csv.DictReader(io.StringIO(text, newline=""), delimiter=delim))


labeled = read_labeled(LABELED)
empty = [r["item_id"] for r in labeled if not (r.get("my_label") or "").strip()]
if empty:
    raise SystemExit(f"{len(empty)} rows have no my_label yet (item_id: {', '.join(empty)}). Fill them in first.")

an = SentimentIntensityAnalyzer()
rows = []
for r in labeled:
    mine = r["my_label"].strip().lower()
    if mine not in VALID:
        raise SystemExit(f"Item {r['item_id']}: my_label must be negative, neutral or positive (got {mine!r}).")
    c = cardiff[r["item_id"]]
    v = vader_label(an, r["text"])
    rows.append(
        {
            "item_id": r["item_id"],
            "text": r["text"],
            "my_label": mine,
            "cardiff_label": c,
            "vader_label": v,
            "cardiff_correct": c == mine,
            "vader_correct": v == mine,
            "models_disagree": c != v,
        }
    )

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

n = len(rows)
print(f"Items: {n}")
print(f"cardiffnlp agrees with you: {sum(r['cardiff_correct'] for r in rows)}/{n}")
print(f"VADER agrees with you:      {sum(r['vader_correct'] for r in rows)}/{n}")
print(f"The two models disagree on: {sum(r['models_disagree'] for r in rows)}/{n}")
print("\nYour labels:", dict(Counter(r["my_label"] for r in rows)))
print("cardiffnlp: ", dict(Counter(r["cardiff_label"] for r in rows)))
print("VADER:      ", dict(Counter(r["vader_label"] for r in rows)))
print(f"\nWrote {OUT}. Read the rows where a model is wrong: those are your failures.")
