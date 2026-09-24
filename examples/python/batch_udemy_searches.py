"""Collect a small combined catalog from several public Udemy searches."""

from __future__ import annotations

import json
import os

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/udemy-course-catalog-scraper"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = {
        "searchUrls": [
            "https://www.udemy.com/courses/search/?src=ukw&q=python",
            "https://www.udemy.com/courses/search/?src=ukw&q=data+science",
        ],
        "maxItems": 10,
        "includeCourseDetails": False,
    }
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    print(json.dumps({"items": len(items), "courses": items}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
