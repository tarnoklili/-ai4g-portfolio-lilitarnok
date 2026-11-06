"""AI Coding Pulse collector.

Polls the Hacker News search API (Algolia) for new comments about AI coding
assistants (Copilot, Cursor, Claude Code and similar),
scores each one with a Hugging Face sentiment transformer that runs locally in
this process, and appends the results to data/items.csv.

Stored per item: HN item id, post time, collection time, text, label, score, model.
NOT stored: usernames, profiles, or anything else that identifies the writer.

Run once:   python collect.py
Scheduled:  see .github/workflows/collect.yml
"""
import csv
import html
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from transformers import pipeline

import config

DATA_FILE = Path("data/items.csv")
FIELDS = ["item_id", "created_at", "collected_at", "text", "label", "score", "model"]
API = "https://hn.algolia.com/api/v1/search_by_date"
TAG_RE = re.compile(r"<[^>]+>")


def clean(raw):
    """HN comments come as HTML. Turn into plain text."""
    text = html.unescape(TAG_RE.sub(" ", raw or ""))
    return re.sub(r"\s+", " ", text).strip()


URL_RE = re.compile(r"https?://\S+")
MENTION_RE = re.compile(r"@\w+")


def prep(text):
    """Model input only (stored text stays as written): the cardiffnlp model card
    says to replace links with 'http' and usernames with '@user' before inference."""
    return MENTION_RE.sub("@user", URL_RE.sub("http", text))


def load_seen():
    seen, newest = set(), 0
    if DATA_FILE.exists():
        with DATA_FILE.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                seen.add(row["item_id"])
                try:
                    ts = int(datetime.fromisoformat(row["created_at"]).timestamp())
                    newest = max(newest, ts)
                except ValueError:
                    pass
    return seen, newest


def fetch(since_ts):
    """Return {item_id: (created_ts, text)} for all queries since since_ts."""
    found = {}
    for query in config.QUERIES:
        page = 0
        while True:
            r = requests.get(
                API,
                params={
                    "query": query,
                    "tags": "comment",
                    "numericFilters": f"created_at_i>{since_ts}",
                    "hitsPerPage": 100,
                    "page": page,
                },
                timeout=30,
            )
            r.raise_for_status()
            data = r.json()
            for hit in data.get("hits", []):
                text = clean(hit.get("comment_text"))
                if len(text) >= config.MIN_CHARS and config.is_relevant(text):
                    found[str(hit["objectID"])] = (hit["created_at_i"], text)
            page += 1
            if page >= data.get("nbPages", 0) or page >= config.MAX_PAGES:
                break
            time.sleep(0.5)
        time.sleep(0.5)
    return found


def main():
    DATA_FILE.parent.mkdir(exist_ok=True)
    seen, newest = load_seen()
    now = int(time.time())

    if newest:
        # Overlap a little so nothing slips between runs; duplicates are skipped by id.
        since = newest - 2 * 3600
    else:
        # No data yet: look back at least 1 hour so the first runs are not empty.
        since = now - max(config.FIRST_RUN_BACKFILL_HOURS, 1) * 3600

    found = fetch(since)
    new = {i: v for i, v in found.items() if i not in seen}
    print(f"fetched {len(found)} matching, {len(new)} new")
    if not new:
        return

    clf = pipeline(
        "text-classification",
        model=config.MODEL_NAME,
        truncation=True,
        max_length=512,
    )
    ids = sorted(new, key=lambda i: new[i][0])
    results = clf([prep(new[i][1]) for i in ids], batch_size=16)

    write_header = not DATA_FILE.exists()
    collected_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            w.writeheader()
        for i, res in zip(ids, results):
            created_ts, text = new[i]
            w.writerow(
                {
                    "item_id": i,
                    "created_at": datetime.fromtimestamp(created_ts, timezone.utc).isoformat(timespec="seconds"),
                    "collected_at": collected_at,
                    "text": text,
                    "label": res["label"],
                    "score": round(res["score"], 4),
                    "model": config.MODEL_NAME,
                }
            )
    print(f"stored {len(ids)} items")


if __name__ == "__main__":
    sys.exit(main())
