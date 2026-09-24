# Run Udemy Course Catalog & Pricing Data Scraper without code

You can use the hosted Actor from the Apify web interface without installing a package or writing a script.

## Step-by-step

1. Open [Udemy Course Catalog & Pricing Data Scraper on Apify](https://apify.com/datascraperes/udemy-course-catalog-scraper?fpr=edudata).
2. Select the **Input** tab.
3. Enter one or more keywords or phrases such as `python` or `data science` in **What do you want to search for?**.
4. Choose the maximum number of unique courses, optionally enable **Only free courses**, and decide whether to include course-page details.
5. Click **Start**.
6. When the run finishes, open **Dataset** and inspect or export JSON, CSV or Excel-compatible data.

## First test

Start with [`data/sample-input.json`](../data/sample-input.json). It requests only three unique courses, so you can verify the shape before sending a larger batch.

## Use the monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors, and no credit card is required to start. Use a small input first so you can test the Actor while credit is available. The credit is not unlimited and unused credit expires at the end of the billing cycle.

See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current terms.

## What to check in the output

Each item should have `recordType: "course"`, a `courseId`, `title`, public course `url`, generated search context, arrays such as `instructors` and `learningOutcomes`, a `price` object when available, and a UTC `scrapedAt` timestamp. Ratings, prices, images and some catalog fields are public snapshots and can be unavailable or change later.

## Larger runs

Use up to 10 search terms and up to 10,000 unique courses across the run. The Actor deduplicates by course ID, continues pagination until the target or source exhaustion, and charges one `course-result` event per unique item successfully written to the Dataset. Optional course-page details add requests for each result.

For repeatable monitoring, use the hosted Actor's saved inputs or scheduling features and review each run's Dataset and status.
