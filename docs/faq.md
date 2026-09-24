# FAQ

## Can I run the Actor without Python or code?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata), enter one or more public Udemy search URLs in the **Input** tab, click **Start** and inspect or export the **Dataset**. See [`docs/no-code-guide.md`](no-code-guide.md).

## What URL should I submit?

Submit a public Udemy course-search URL containing a `q` query, for example `https://www.udemy.com/courses/search/?src=ukw&q=python`. You can submit 1–10 unique search URLs and preserve public filters included in those URLs.

## Can I test it with Apify's Free plan?

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors. It can cover a small test while credit is available, but it is not unlimited free usage. Unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for the current terms.

## How do I scrape several Udemy topics in one run?

Add several search URLs to `searchUrls` and set `maxItems` to the total unique-course target. The Actor deduplicates courses across targets and retains `sourceSearchUrl` and `page` for provenance. See [`examples/python/batch_udemy_searches.py`](../examples/python/batch_udemy_searches.py).

## How do I export Udemy course prices to CSV?

Use the Dataset export controls in Apify or [`examples/python/export_udemy_courses.py`](../examples/python/export_udemy_courses.py). Keep `price`, `scrapedAt` and the currency fields because public prices are market- and time-sensitive.

## What does `includeCourseDetails` do?

When `true`, the Actor requests available structured details from each public course page, such as description, publication date, language, offers, syllabus sections and audience. It increases request count and run time. If the optional page cannot provide details, the primary course record remains and reports `detailStatus: "not_available"`.

## How is the run billed?

The primary event is `course-result`: one unique public course successfully written to the default Dataset. The configured prices range from $0.00100 per result on FREE to $0.00075 on the highest tiers. Duplicates, failed requests and records not written to the Dataset do not create that event. Check the [Actor pricing page](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata) for current terms.
