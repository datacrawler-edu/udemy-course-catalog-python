"""Run the Actor and export a useful flat course view to CSV."""

from __future__ import annotations

import csv
import os
from pathlib import Path

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/udemy-course-catalog-scraper"
ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
OUTPUT_PATH = ROOT / "data" / "exported-udemy-courses.csv"
FIELDS = [
    "courseId",
    "title",
    "url",
    "locale",
    "level",
    "ratingAverage",
    "ratingCount",
    "durationSeconds",
    "lectureCount",
    "isFree",
    "priceAmount",
    "priceCurrency",
    "priceString",
    "scrapedAt",
]


def flatten(item: dict) -> dict[str, object]:
    price = item.get("price") or {}
    return {
        "courseId": item.get("courseId"),
        "title": item.get("title"),
        "url": item.get("url"),
        "locale": item.get("locale"),
        "level": item.get("level"),
        "ratingAverage": item.get("ratingAverage"),
        "ratingCount": item.get("ratingCount"),
        "durationSeconds": item.get("durationSeconds"),
        "lectureCount": item.get("lectureCount"),
        "isFree": item.get("isFree"),
        "priceAmount": price.get("amount"),
        "priceCurrency": price.get("currency"),
        "priceString": price.get("priceString"),
        "scrapedAt": item.get("scrapedAt"),
    }


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    import json

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    items = client.dataset(run["defaultDatasetId"]).iterate_items()

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(flatten(item) for item in items)

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
