# Udemy course catalog scraper with Python

Run **Udemy Course Catalog & Pricing Data Scraper** from Apify's web interface without writing code, or call it from Python, JavaScript or cURL to receive structured public Udemy course records.

This repository contains request examples, a small input, a real sanitized Dataset item and CSV data. It documents the hosted Actor; it does not contain the Actor's private runtime source.

[Open Udemy Course Catalog & Pricing Data Scraper on Apify](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata)

## What this repository helps you do

- Turn one or more Udemy keywords or phrases into a deduplicated course catalog.
- Compare titles, ratings, instructors, learning outcomes, curriculum counts and public price snapshots.
- Build research, education-data, SEO and catalog workflows from JSON or CSV output.
- Optionally request structured public details from each returned course page.

## Example result

The repository includes a sanitized example in [`data/sample-output.json`](data/sample-output.json) and a tabular version in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "recordType": "course",
  "courseId": "2776760",
  "title": "100 Days of Code™: The Complete Python Pro Bootcamp",
  "url": "https://www.udemy.com/course/100-days-of-code",
  "ratingAverage": 4.671892166137695,
  "ratingCount": 436596,
  "lectureCount": 604,
  "price": {
    "amount": 329000,
    "currency": "VND",
    "priceString": "₫329,000"
  }
}
```

Prices, ratings, counts and timestamps are snapshots from the run and can change on Udemy.

## Run without code

You can run the hosted Actor directly from the Apify web interface.

1. Open [Udemy Course Catalog & Pricing Data Scraper on Apify](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata).
2. In the **Input** tab, enter one or more Udemy keywords or phrases.
3. Set the maximum number of unique courses, choose the available catalog filters from their predefined dropdowns or multiselects, optionally select free courses, and decide whether to include course-page details.
4. Click **Start**.
5. Open the **Dataset** tab and export JSON, CSV or Excel-compatible data.

Use [`docs/no-code-guide.md`](docs/no-code-guide.md) for the field-by-field walkthrough and [`data/sample-input.json`](data/sample-input.json) for a small first test.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors. No credit card is required to start, but the credit is limited and unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) before larger runs.

## Quick start for developers

### Python

```bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/request.py
```

On Windows PowerShell:

```powershell
pip install -r examples/python/requirements.txt
$env:APIFY_API_TOKEN = "your-token"
python examples/python/request.py
```

The example reads [`data/sample-input.json`](data/sample-input.json), starts the hosted Actor and prints the returned Dataset items. A live run consumes the Actor's public pay-per-event pricing.

## Input example

```json
{
  "searchTerms": ["python"],
  "maxItems": 3,
  "freeOnly": false,
  "sortOrder": "RATING",
  "languages": ["EN"],
  "minRating": 4.5,
  "includeCourseDetails": false
}
```

See the complete field guide in [`docs/input-reference.md`](docs/input-reference.md).

## Request examples

### cURL

See [`examples/curl-request.md`](examples/curl-request.md) for a synchronous API request.

### Python

See [`examples/python/request.py`](examples/python/request.py), [`examples/python/batch_udemy_searches.py`](examples/python/batch_udemy_searches.py) and [`examples/python/export_udemy_courses.py`](examples/python/export_udemy_courses.py).

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

All examples call the hosted Apify Actor. They do not expose a proxy, bypass access controls or require the Actor source code locally.

## Output fields

The default Dataset writes one item for each unique public course successfully collected:

| Field | Meaning |
| --- | --- |
| `courseId`, `title`, `url` | Stable public course identity and landing page. |
| `sourceSearchUrl`, `page` | Search target and page that produced the record. |
| `ratingAverage`, `ratingCount`, `locale`, `level` | Public catalog signals when available. |
| `durationSeconds`, `lectureCount`, `practiceTestQuestionsCount` | Curriculum and duration counts. |
| `instructors`, `learningOutcomes`, `badges`, `images` | Public course metadata arrays and image URLs. |
| `price` | Current public price snapshot with amount, currency and display string when available. |
| `scrapedAt` | UTC capture timestamp. |
| `detailStatus` and optional detail fields | Present when course-page enrichment is requested; unavailable details are marked rather than invented. |

See [`docs/output-reference.md`](docs/output-reference.md) for the complete output contract.

## Common use cases

Read [`docs/use-cases.md`](docs/use-cases.md) for complete workflows covering:

- topic and competitor course research;
- price and rating snapshots;
- SEO or training-catalog enrichment.

## How to scrape Udemy course search results with Python

Use [`examples/python/request.py`](examples/python/request.py) with one or more keywords or phrases. Submit several terms in one input when you need a combined catalog; the Actor deduplicates courses across targets.

## How to export Udemy course prices and ratings to CSV

Use [`examples/python/export_udemy_courses.py`](examples/python/export_udemy_courses.py) or export the completed Dataset from Apify. Keep `scrapedAt`, `price.currency` and `price.priceString` with the records because promotions and currencies can vary by market and time.

## FAQ

See [`docs/faq.md`](docs/faq.md) for questions derived from the real input, output and billing contract.

## Limits and pricing

Submit 1–10 unique Udemy keywords or phrases, each up to 200 characters. `maxItems` defaults to 100 and accepts 1–10,000 unique courses across all terms. `freeOnly` defaults to `false`; `includeCourseDetails` defaults to `false` and can increase request count and run time. Optional catalog filters include predefined `sortOrder` (`RELEVANCE`, `REVIEWS`, `RATING`, `TIME`), ISO-639-1 language multiselects, Udemy level and video-length multiselects, `minRating` in half-point increments, and boolean requirements for captions, quizzes, coding exercises, practice tests, workspaces, roleplays, certification preparation and practice-test-only courses. The web UI prevents invalid selector values; JSON and API callers must use the exact enum values documented below.

The Actor charges one `course-result` event for each unique public course successfully written to the default Dataset. The current configured tier range is **$0.00100–$0.00075 per result**, equivalent to **$1.00–$0.75 per 1,000 courses** depending on the Apify tier. Failed requests, duplicates and records not written to the Dataset do not create that event. See the [Actor pricing page](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata) for the active terms.

## Hosted version

Use the hosted version when you need repeatable execution, multiple search targets, scheduling, API access or Dataset storage without managing scraping infrastructure:

[Open Udemy Course Catalog & Pricing Data Scraper on Apify](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata)

## Responsible use

Use the returned data lawfully and respect Udemy's terms, access rules, intellectual-property rights and applicable privacy obligations. This integration is for publicly available course information; it does not access private accounts, enrolled courses, transcripts or protected lesson content. Never commit API tokens or other credentials to this repository.

## Support

For a problem with the examples, [open a GitHub issue](https://github.com/datacrawler-edu/udemy-course-catalog-python/issues) with the command, sanitized input and error message. For an execution problem, include the Apify run ID but never include your token.

## License

This repository is released under the MIT License.
