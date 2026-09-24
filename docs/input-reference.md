# Input reference

The Actor accepts a JSON object with one required list and two optional controls.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `searchUrls` | array of strings | Yes | `["https://www.udemy.com/courses/search/?q=python"]` | 1–10 unique public Udemy course-search URLs. Include `q`; public filters such as `price=price-free` are preserved. |
| `maxItems` | integer | No | `3` | Maximum number of unique courses written across all URLs. Default `100`; range `1`–`10000`. |
| `includeCourseDetails` | boolean | No | `false` | Request available structured fields from each public course page. Default `false`; increases request count and run time. |

## Smallest useful input

```json
{
  "searchUrls": [
    "https://www.udemy.com/courses/search/?src=ukw&q=python"
  ],
  "maxItems": 3,
  "includeCourseDetails": false
}
```

## Validation and limits

- `searchUrls` must contain 1–10 unique non-empty values.
- Each search URL should be a public Udemy course-search URL with a `q` parameter.
- `maxItems` is a unique-course limit across all submitted URLs, not a page limit.
- Pagination continues until the target is reached or the public catalog is exhausted.
- There are no mutually exclusive fields.
- Large limits and optional detail enrichment require more requests and may take longer.
