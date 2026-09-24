# cURL request

Set `APIFY_API_TOKEN` in your shell and keep it out of source files and command history where possible.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~udemy-course-catalog-scraper/run-sync-get-dataset-items" \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

The synchronous endpoint waits for the run to finish and returns the default Dataset items. For longer jobs, start the asynchronous run endpoint and read the Dataset after completion. A live request uses the hosted Actor's public pay-per-event pricing.
