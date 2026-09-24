"""Run the hosted Udemy Actor and print its Dataset items."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/udemy-course-catalog-scraper"
ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
